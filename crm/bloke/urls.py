from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.user_logout, name="user_logout"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("create_record", views.create_record, name="create_record"),
    path("update_record/<str:pk>/", views.update_record, name="update_record"),
    path("record/<str:pk>/", views.single_record, name="record"),
]
