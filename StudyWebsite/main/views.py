from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import StudyGroup 

# Create your views here.
def index_view(request: HttpRequest):

    return render(request, "main/index.html")


def group_dashboard(request:HttpRequest , group_id):
  group=StudyGroup.objects.get(id=group_id)
  

  return render(request,"main/group_dashboard.html" , {"group":group })


def user_dashboard(request:HttpRequest):

  return render(request,"main/user_dashboard.html")




def create_group(request:HttpRequest):
  if request.method =="POST":
    try:
     new_group=StudyGroup(
      creator=request.user,
      name=request.POST["name"],
      description=request.POST["description"],
      icon=request.FILES.get("icon"),
            )
     new_group.save()
    except Exception as e:
            print(e)
    return redirect('main:user_dashboard_view')

  return render(request,"main/create_group.html")


def delete_group(request:HttpRequest , group_id):
  try:
    group=StudyGroup.objects.get(pk=group_id)
    group.delete()
  except StudyGroup.DoesNotExist:
    group=None
  except Exception as e:
    print(e)
  return redirect('main:user_dashboard_view')
