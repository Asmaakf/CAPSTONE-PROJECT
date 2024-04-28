from django.urls import path
from . import views

app_name  = "accounts"

urlpatterns = [
    path("register/", views.user_register_view, name="user_register_view"),
    path("login/", views.user_login_view, name="user_login_view"),
    path("logout/", views.user_logout_view, name="user_logout_view"),
    path("profile/<user_name>/", views.user_profile_view, name="user_profile_view"),
    path('update/<int:user_id>/', views.update_user_profile_view, name='update_user_profile_view'),
    path('delete_user_profile/', views.delete_user_profile, name='delete_user_profile'),
]