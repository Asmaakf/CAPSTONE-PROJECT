from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from datetime import date, timedelta
from .models import ReviewSet, FlashCard
from main.models import StudyGroup


# Create your views here.


# Review Set views
def add_set_view(request: HttpRequest,group_id):
    
    if request.method == 'POST':

        if request.user.is_authenticated:
            try:
                group=StudyGroup.objects.get(pk=group_id)
                new_set = ReviewSet(
                    title = request.POST["title"],
                    description = request.POST["description"],
                    created_by = request.user,
                )
                new_set.save()  
                return redirect("review_sets:all_sets_view",group_id=group.id) ##pop up successfully
            except Exception as e:
                print(e)
    return render(request, "review_sets/add_set.html")



def update_set_view(request: HttpRequest, set_id,group_id):

    #limit access to this view for only staff
    group=StudyGroup.objects.get(pk=group_id)
    #update
    r_set = ReviewSet.objects.get(pk=set_id)
    if request.method == "POST":
        try:
            r_set.title = request.POST["title"]
            r_set.description = request.POST["description"]
            r_set.save()
            return redirect("review_sets:full_set_view", set_id = r_set.id, group_id=group.id)
        except Exception as e:
            print(e)
    return render(request, "review_sets/update_set.html", {"r_set" : r_set,"group":group})


def delete_set_view(request: HttpRequest, set_id,group_id ):
    group=StudyGroup.objects.get(pk=group_id)
    #limit access to this view for only staff
    try:
        r_set = ReviewSet.objects.get(pk=set_id)
        r_set.delete()
    except Exception as e:
        print(e)
    return redirect("review_sets:all_sets_view",group_id=group.id)


def all_sets_view(request: HttpRequest,group_id):
    group=StudyGroup.objects.get(pk=group_id)
    sets= ReviewSet.objects.filter(group=group)
    return render(request, "review_sets/all_sets.html", {"sets": sets,"group":group} )


def full_set_view(request: HttpRequest, set_id): #  set detail
    try:
        review_set = ReviewSet.objects.get(pk=set_id)
        cards = FlashCard.objects.filter(review_set=review_set)

    except ReviewSet.DoesNotExist:
        review_set = None
    except Exception as e:
        print(e)

    return render(request, "review_sets/full_set.html", {"review_set" : review_set, "cards" : cards})




####################### FlashCard views ##########################

def add_card_view(request: HttpRequest, set_id):

    if request.method == 'POST':

        if request.user.is_authenticated:    
            try:
                review_set = ReviewSet.objects.get(pk=set_id)
                new_card = FlashCard(
                    question = request.POST["question"],
                    answer = request.POST["answer"],
                    review_set = review_set,
                )

                new_card.save()  
                return redirect("review_sets:full_set_view", set_id=review_set.id) ##pop up successfully
            except Exception as e:
                print(e)

    return render(request, "review_sets/full_set.html")



def update_card_view(request: HttpRequest, set_id, card_id):
    
    review_set = ReviewSet.objects.get(pk=set_id)
    card = FlashCard.objects.get(pk=card_id)

    if request.method == "POST":

        try:
            card.question = request.POST["question"],
            card.answer = request.POST["answer"]
            card.save()
            return redirect ("review_sets:full_set_view", set_id=review_set.id)
        except Exception as e:
            print(e)
    return render(request, 'review_sets/full_set.html',{"review_set" : review_set, "card" : card})



def delete_card_view(request: HttpRequest, set_id, card_id):

     #limit access to this view for only staff
   
    review_set = ReviewSet.objects.get(pk=set_id)
    try:
        card = FlashCard.objects.get(pk=card_id)
        card.delete()
    except FlashCard.DoesNotExist:
        card = None
    except Exception as e:
        print(e)

    return redirect("review_sets:full_set_view", set_id=review_set.id)
    