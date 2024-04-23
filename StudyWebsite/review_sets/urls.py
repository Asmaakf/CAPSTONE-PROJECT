from django.urls import path
from . import views

app_name  = "review_sets"

urlpatterns = [
    path("add/set/", views.add_set_view, name="add_set_view"),
    path("all/sets/<group_id>", views.all_sets_view, name="all_sets_view"),
    path("add/card/", views.add_card_view, name="add_card_view"),
    path("all/set/cards", views.all_set_cards_view, name="all_set_cards_view"),
]