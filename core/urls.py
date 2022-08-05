# Authencation libs
from django.contrib import auth
from django.contrib.auth import views as auth_views

from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="index"),

    # Authentication
    path("signup", SignUpView.as_view(template_name="registration/signup.html"), name="signup"),
    path("login", auth_views.LoginView.as_view(template_name="access/login.html"), name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
]