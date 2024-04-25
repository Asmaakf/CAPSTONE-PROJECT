from django.urls import path
from . import views

app_name  = "review_sets"

urlpatterns = [
    path("add/set/", views.add_set_view, name="add_set_view"),
    path("all/sets/", views.all_sets_view, name="all_sets_view"),
    path("update/set/<set_id>/", views.update_set_view, name="update_set_view"),
    path("full/set/<set_id>/", views.full_set_view, name="full_set_view"),
    path("delete/set/<set_id>/", views.delete_set_view, name="delete_set_view"),
    path("add/card/", views.add_card_view, name="add_card_view"),
]