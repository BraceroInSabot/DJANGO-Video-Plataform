# Authencation libs
from django.contrib.auth import views as auth_views

from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),

    # Authentication
    path("signup", SignUpView.as_view(), name="signup"),
    path("login", auth_views.LoginView.as_view(template_name="access/login.html"), name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("dashboard", dashboard, name="dashboard"),

    #Hall
    path("halloffame/create", CreateHall.as_view(), name="create_hall"),
    path("halloffame/<int:pk>", DetailHall.as_view(), name="detail_hall"),
    path("halloffame/<int:pk>/update", UpdateHall.as_view(), name="update_hall"),
    path("halloffame/<int:pk>/delete", DeleteHall.as_view(), name="delete_hall"),
]