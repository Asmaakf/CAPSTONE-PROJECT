from django.urls import path
from . import views

app_name  = "review_sets"

urlpatterns = [
    path("add/set/<group_id>/", views.add_set_view, name="add_set_view"),
    path("all/sets/<group_id>/", views.all_sets_view, name="all_sets_view"),
    path("update/set/<set_id>/<group_id>/", views.update_set_view, name="update_set_view"),
    path("full/set/<set_id>/", views.full_set_view, name="full_set_view"),
    path("delete/set/<set_id>/<group_id>/", views.delete_set_view, name="delete_set_view"),

    path("add/card/<set_id>/", views.add_card_view, name="add_card_view"),
    path("delete/card/<set_id>/<card_id>/", views.delete_card_view, name="delete_card_view"),
    path("update/card/<set_id>/<card_id>/", views.update_card_view, name="update_card_view"),


]