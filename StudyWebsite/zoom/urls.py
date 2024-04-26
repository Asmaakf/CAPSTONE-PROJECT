from django.urls import path
from . import views

app_name  = "zoom"

urlpatterns = [
    path("session/", views.zoom_session_view, name="zoom_session_view"),

]