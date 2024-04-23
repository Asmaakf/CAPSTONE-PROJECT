from django.urls import path
from . import views

app_name  = "contact"

urlpatterns = [
    path("contact/", views.contact_view, name="contact_view"),
    path("contact/messages/", views.message_view, name="message_view"),
    path("delete/<msg_id>/", views.delete_message_view, name="delete_message_view")
]