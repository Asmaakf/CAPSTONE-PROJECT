from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

#import User Model
from django.contrib.auth.models import User


#import login, logout, authenticate
from django.contrib.auth import authenticate, login, logout


#import transaction
from django.db import transaction, IntegrityError


# Create your views here.

def user_register_view(request:HttpRequest):
    msg = None

    if request.method == "POST":
        try:
            #create new user
            new_user = User.objects.create_user(
                username=request.POST["username"], 
                email=request.POST["email"], 
                first_name=request.POST["first_name"], 
                last_name=request.POST["last_name"], 
                password=request.POST["password"]
            )
            new_user.save()

            #redirect to login page
            return redirect("accounts:user_login_view")
        
        except IntegrityError as e:
            msg = "Username already exists. Please choose a different username."
            print(e)

        except Exception as e:
            msg = "Something went wrong. Please try again."
            print(e)
    
    return render(request, "accounts/user_register.html", {"msg" : msg})



def user_login_view(request:HttpRequest):
    msg = None

    if request.method == "POST":

        #authenticat user
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if user:
            #login user
            login(request, user)
            return redirect("main:index_view")
        else:
            msg = "username or Password is wrong. Try again..."
    
    return render(request, "accounts/user_login.html", {"msg" : msg})



def user_logout_view(request:HttpRequest):
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('accounts:user_login_view')

