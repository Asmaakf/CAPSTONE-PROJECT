from django.urls import path
from . import views

app_name  = "attachments"

urlpatterns = [
   path("attachment/", views.attachment_view, name="attachment_view"),
]