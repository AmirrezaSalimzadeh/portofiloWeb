from django.shortcuts import render
from .utils import randomQuote
# Create your views here.
def Home(request):
    return render(request,"Home.html")
def about(request):
    return render(request,"about.html")
def quote(request):
    return render(request,"qoutes.html",{"qoutes" :randomQuote()})