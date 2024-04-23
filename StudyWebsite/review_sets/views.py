from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from datetime import date, timedelta
from .models import ReviewSet, FlashCard
from main.models import StudyGroup


# Create your views here.


# Review Set views
def add_set_view(request: HttpRequest, group_id):

    if request.method == 'POST':

        if request.user.is_authenticated:
            try:
                group = StudyGroup.objects.get(pk=group_id)
                new_set = ReviewSet(
                    title = request.POST["title"],
                    description = request.POST["description"],
                    created_by = request.user,
                    group = group
                )

                new_set.save()  
                return redirect("review_sets:all_sets_view", group_id=group.id) ##pop up successfully
            except Exception as e:
                print(e)

    return render(request, "review_sets/add_set.html")



def update_set_view(request: HttpRequest):
    pass

def delete_set_view(request: HttpRequest):
    pass

def all_sets_view(request: HttpRequest):

    sets = ReviewSet.objects.all()

    return render(request, "review_sets/all_sets.html", {"sets" : sets})



# FlashCard views
def add_card_view(request: HttpRequest):

    if request.method == 'POST':

        try:
            new_card = FlashCard(
                question = request.POST["question"],
                answer = request.POST["answer"],
            )
            new_card.save()  
            return redirect("review_sets:all_set_cards_view") ##pop up successfully
        except Exception as e:
            print(e)

    return render(request, "review_sets/add_card.html")


def update_card_view(request: HttpRequest):
    pass

def delete_card_view(request: HttpRequest):
    pass

def all_set_cards_view(request: HttpRequest):

    cards = FlashCard.objects.all()

    return render(request, "review_sets/all_set_cards.html", {"cards" : cards})

