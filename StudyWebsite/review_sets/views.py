from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from datetime import date, timedelta
from .models import ReviewSet, FlashCard
from main.models import StudyGroup


# Create your views here.


# Review Set views
def add_set_view(request: HttpRequest):

    if request.method == 'POST':

        if request.user.is_authenticated:
            try:
                new_set = ReviewSet(
                    title = request.POST["title"],
                    description = request.POST["description"],
                    created_by = request.user,
                )
                new_set.save()  
                return redirect("review_sets:all_sets_view") ##pop up successfully
            except Exception as e:
                print(e)
    return render(request, "review_sets/add_set.html")



def update_set_view(request: HttpRequest, set_id):

    #limit access to this view for only staff

    #update
    r_set = ReviewSet.objects.get(pk=set_id)
    if request.method == "POST":
        try:
            r_set.title = request.POST["title"]
            r_set.description = request.POST["description"]
            r_set.save()
            return redirect("review_sets:full_set_view", set_id = r_set.id)
        except Exception as e:
            print(e)
    return render(request, "review_sets/update_set.html", {"r_set" : r_set})


def delete_set_view(request: HttpRequest, set_id ):

    #limit access to this view for only staff
   
    try:
        r_set = ReviewSet.objects.get(pk=set_id)
        r_set.delete()
    except Exception as e:
        print(e)
    return redirect("review_sets:all_sets_view")


def all_sets_view(request: HttpRequest):
    sets= ReviewSet.objects.all()
    return render(request, "review_sets/all_sets.html", {"sets": sets } )



####################### FlashCard views ##########################

# FlashCard views
def add_card_view(request: HttpRequest):

    if request.method == 'POST':

        try:
            new_card = FlashCard(
                question = request.POST["question"],
                answer = request.POST["answer"],
            )
            new_card.save()  
            return redirect("review_sets:all_cards_view") ##pop up successfully
        except Exception as e:
            print(e)

    return render(request, "review_sets/add_card.html")


def update_card_view(request: HttpRequest):
    pass

def delete_card_view(request: HttpRequest):
    pass

def full_set_view(request: HttpRequest): # containe set detail

    cards = FlashCard.objects.all()

    return render(request, "review_sets/full_set.html", {"cards" : cards})

