from django.urls import path
from . import views

app_name  = "main"

urlpatterns = [
    path("", views.index_view, name="index_view"),
    path("group/",views.group_dashboard,name="group_dashboard_view"),
    path("user/dashboard/",views.user_dashboard,name="user_dashboard_view"),
]