from django.urls import path
from . import views

app_name  = "todo_list"

urlpatterns = [
   path("todo/<user_id>/", views.add_todo_view, name="add_todo_view"),
   path("todo/<user_id>/", views.all_todo_view, name="all_todo_view"),
   path('delete/<todo_id>/<user_id>/',views.delete_todo_view, name="delete_todo_view"),
   path('update/<todo_id>/<user_id>/',views.update_todo_view, name="update_todo_view")
]