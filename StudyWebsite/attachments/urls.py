from django.urls import path
from . import views

app_name  = "attachments"

urlpatterns = [
   path("attachments/<group_id>/", views.add_attachment_view, name="add_attachment_view"),
   path("attach/<group_id>/", views.all_attachment_view, name="all_attachment_view"),
   path('delete/<attachment_id>/<group_id>/',views.delete_attachment_view, name="delete_attachment_view"),
   path('update/<attachment_id>/<group_id>/',views.update_attachment_view, name="update_attachment_view")
]