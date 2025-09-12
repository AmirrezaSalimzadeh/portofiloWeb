from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="home"),
    path("home/", views.Home, name="home"),
    path("about/", views.about, name="about"),
    path("quote/",views.quote,name= "quote"),
]