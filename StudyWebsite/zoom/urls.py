from django.urls import path
from . import views

app_name  = "zoom"

urlpatterns = [
    path("session/<group_id>/<user_id>/", views.create_zoom_meeting_view, name="create_zoom_meeting_view"),

]