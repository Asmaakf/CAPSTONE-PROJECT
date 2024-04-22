from django.urls import path
from . import views

app_name  = "accounts"

urlpatterns = [
    path("register/", views.user_register_view, name="user_register_view"),
    path("login/", views.user_login_view, name="user_login_view"),
    path("logout/", views.user_logout_view, name="user_logout_view"),
]