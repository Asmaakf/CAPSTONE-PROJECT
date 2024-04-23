from django.urls import path
from . import views

app_name  = "main"

urlpatterns = [
    path("", views.index_view, name="index_view"),
    path("group/<group_id>/",views.group_dashboard,name="group_dashboard_view"),
    path("user/dashboard/",views.user_dashboard,name="user_dashboard_view"),
    path("create/group/",views.create_group,name="create_group_view"),
    path("delete/<group_id>/group/",views.delete_group,name="delete_group_view"),
]