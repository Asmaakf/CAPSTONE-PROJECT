from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

#import User Model
from django.contrib.auth.models import User


#import login, logout, authenticate
from django.contrib.auth import authenticate, login, logout


#import transaction
from django.db import transaction, IntegrityError

# import profile
from .models import Profile

# delete
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden



# Create your views here.

# register
def user_register_view(request:HttpRequest):
    msg = None

    if request.method == "POST":
        try:
            with transaction.atomic():
                #create new user
                new_user = User.objects.create_user(
                    username=request.POST["email"],  
                    first_name=request.POST["first_name"], 
                    last_name=request.POST["last_name"], 
                    password=request.POST["password"]
                )
                new_user.save()
                profile = Profile(user=new_user,birthdate = request.POST["birthdate"])
                profile.save()

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
        user = authenticate(request, username=request.POST["email"], password=request.POST["password"])

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



# profile
def user_profile_view(request:HttpRequest, user_name):

    user = User.objects.get(username=user_name)
    
    return render(request, "accounts/user_profile.html", {"user" : user})



# update profile
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib.auth.models import User
from accounts.models import Profile

def update_user_profile_view(request: HttpRequest, user_id):
    msg = None

    if not request.user.is_authenticated:
        return redirect("accounts:user_login_view")
    
    try:
        user_info = User.objects.get(pk=user_id)
    except:
        return render(request,'main/not_found.html')
    
    if request.method == "POST":
        
        try:
            with transaction.atomic():
                user: User = request.user
                user.first_name = request.POST["first_name"]
                user.last_name = request.POST["last_name"]
                user.save()
            
                try:
                    profile: Profile = user.profile
                except Profile.DoesNotExist: 
                    profile = Profile(user=user)

                profile.avatar = request.FILES.get("avatar", profile.avatar)
                profile.birthdate = request.POST.get("birthdate")
                profile.bio = request.POST["bio"]
                profile.linkedin_link = request.POST["linkedin_link"]
                profile.github_link = request.POST["github_link"]
                profile.save()

                
                return redirect("main:user_dashboard_view", user_id=user.id)

        except Exception as e:
            msg = f"حدث خطأ ما: {e}"
            print(f"Error for user ID {user_id}: {e}")

    return render(request, "accounts/update_user_profile.html", {"user_info":user_info,"msg": msg})

