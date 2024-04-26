from django.urls import path
from . import views

app_name  = "main"

urlpatterns = [
    path("", views.index_view, name="index_view"),
    path("all/groups/", views.all_groups_view, name="all_groups_view"),
    path("group/<group_id>/<user_id>/",views.group_dashboard,name="group_dashboard_view"),
    path("user/dashboard/<user_id>/",views.user_dashboard,name="user_dashboard_view"),
    path("create/group/<user_id>/",views.create_group,name="create_group_view"),
    path("delete/<group_id>/group/",views.delete_group,name="delete_group_view"),
    path("requests/<group_id>/",views.member_request_view,name="member_request_view"),
    path("user/requests/<user_id>/<request_id>/",views.accept_reject_member_request_view,name="accept_reject_member_request_view"),
    path("remove/member/<user_id>/<request_id>/<group_id>/",views.remove_member_view,name="remove_member_view"),
    path("disction/<group_id>/",views.discussion_view,name="discussion_view"),
    path("delete/disction/<group_id>/<msg_id>/",views.delete_discussion_view,name="delete_discussion_view"),
    path("not/found/", views.not_found_view, name="not_found_view"),
    path("not/allowed/", views.not_allowed_view, name="not_allowed_view"),
]