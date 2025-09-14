from django.shortcuts import render,redirect
from .utils import randomQuote
from .models import Quotes
# Create your views here.
def Home(request):
    author, quote1 = randomQuote()
    return render(request, "Home.html", {"quote": quote1, "author": author})

def about(request):
    return render(request,"about.html")

def add_quote(request):
    if request.method == "POST":  # when the form is submitted
        content = request.POST.get("quote")
        author = request.POST.get("author")
        Quotes.objects.create(content=content, author=author)
        return redirect("home")  # after saving
    return render(request, "add_quotes.html")