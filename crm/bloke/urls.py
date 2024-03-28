from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.user_logout, name="user_logout"),
    path("dashboard", views.dashboard, name="dashboard"),
]
