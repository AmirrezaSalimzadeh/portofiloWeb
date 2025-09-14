from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .utils import randomQuote
from .models import Quotes

# Create your views here.
def Home(request):
    author, quote = randomQuote()
    return render(request, "Home.html", {"quote": quote, "author": author})

def about(request):
    return render(request,"about.html")

def add_quote(request):
    if request.method == "POST":  # when the form is submitted
        content = request.POST.get("quote")
        author = request.POST.get("author")
        Quotes.objects.create(content=content, author=author)
        return redirect("home")  # after saving
    return render(request, "add_quotes.html")

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        if password != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, "signup.html")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, "signup.html")
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect("home")
    return render(request, "signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "signin.html")
    return render(request, "signin.html")

def signout(request):
    logout(request)
    return redirect("home")