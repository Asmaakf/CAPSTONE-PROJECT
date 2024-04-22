from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


# Create your views here.
def index_view(request: HttpRequest):

    return render(request, "main/index.html")


def group_dashboard(request:HttpRequest):

  return render(request,"main/group_dashboard.html")


def user_dashboard(request:HttpRequest):

  return render(request,"main/user_dashboard.html")