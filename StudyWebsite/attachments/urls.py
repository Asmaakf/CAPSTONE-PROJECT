from django.urls import path
from . import views

app_name  = "attachments"

urlpatterns = [
   path("attachments/<group_id>/", views.attachment_view, name="attachment_view"),
   path('delete/<attachment_id>/',views.delete_attachment, name="delete_attachment"),
   path('update/<attachment_id>/',views.update_attachment, name="update_attachment")
]