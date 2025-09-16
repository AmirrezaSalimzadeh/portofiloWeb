from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="home"),
    path("home/", views.Home, name="home"),
    path("about/", views.about, name="about"),
    path("add_quote/", views.add_quote, name="add_quote"),
    path("change_quote/", views.change_quote, name="change_quote"),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),
    path("api/check-username/", views.check_username, name="check_username"),
]
