from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="home"),
    path("home/", views.Home, name="home"),
    path("about/", views.about, name="about"),
    path("add_quote/", views.add_quote, name="add_quote"),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),
]