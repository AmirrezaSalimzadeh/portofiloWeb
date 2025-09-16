from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .utils import randomQuote
from .models import Author, Quotes, Tag

# Create your views here.
def Home(request):
    quote_payload = randomQuote()
    context = {}
    if quote_payload:
        quote_obj = quote_payload["quote"]
        category = quote_payload["category"] or "Uncategorized"
        context = {
            "quote_obj": quote_obj,
            "category": category,
        }
    return render(request, "Home.html", context)

def about(request):
    return render(request,"about.html")

def add_quote(request):
    tags = Tag.objects.select_related("category").order_by("category__name", "name")
    if request.method == "POST":  # when the form is submitted
        content = request.POST.get("quote", "").strip()
        author_name = request.POST.get("author", "").strip()
        selected_tag_ids = request.POST.getlist("tags")
        if not content or not author_name:
            messages.error(request, "Quote and author are required.")
            return render(
                request,
                "add_quotes.html",
                {
                    "tags": tags,
                    "selected_tags": selected_tag_ids,
                    "quote_text": content,
                    "author_name": author_name,
                },
            )
        author, _ = Author.objects.get_or_create(name=author_name)
        quote = Quotes.objects.create(content=content, author=author)
        if selected_tag_ids:
            valid_tags = Tag.objects.filter(id__in=selected_tag_ids)
            quote.tags.set(valid_tags)
        messages.success(request, "Quote added successfully!")
        return redirect("home")  # after saving
    return render(request, "add_quotes.html", {"tags": tags, "selected_tags": []})


@login_required
def change_quote(request):
    quotes = (
        Quotes.objects.select_related("author")
        .prefetch_related("tags__category")
        .order_by("-created_at")
    )
    return render(request, "change_quote.html", {"quotes": quotes})

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")  # Get email from form
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        if password != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, "signup.html")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, "signup.html")
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return render(request, "signup.html")
        user = User.objects.create_user(username=username, password=password, email=email)
        login(request, user)
        return redirect("home")
    return render(request, "signup.html")

def signin(request):
    if request.method == "POST":
        identifier = request.POST.get("identifier")  # username or email
        password = request.POST.get("password")
        user = None
        # Try to get user by username
        user_obj = User.objects.filter(username=identifier).first()
        if not user_obj:
            # Try to get user by email
            user_obj = User.objects.filter(email=identifier).first()
        if user_obj:
            user = authenticate(request, username=user_obj.username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username/email or password.")
            return render(request, "signin.html")
    return render(request, "signin.html")

def signout(request):
    logout(request)
    return redirect("home")


@require_GET
def check_username(request):
    username = request.GET.get("username", "").strip()
    is_available = bool(username) and not User.objects.filter(username=username).exists()
    return JsonResponse({"available": is_available})
