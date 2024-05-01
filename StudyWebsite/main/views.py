from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import StudyGroup ,MembershipeRequesite , Discussion
from django.contrib.auth.models import User
from django.contrib import messages
from todo_list .models import ToDoList
from zoom .models import ZoomMeeting
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime ,timedelta 
from attachments .models import Attachment

# Create your views here.
def index_view(request: HttpRequest):

    return render(request, "main/index.html")


def all_groups_view(request: HttpRequest):
   all_group=StudyGroup.objects.all
   return render(request, "main/all_groups.html",{"all_group":all_group})

def group_dashboard(request:HttpRequest , group_id , user_id):
  
  
  user=User.objects.get(pk=user_id)
  group=StudyGroup.objects.get(pk=group_id)
  member=MembershipeRequesite.objects.filter(member=user)
  members=MembershipeRequesite.objects.filter(group=group_id)
  users = User.objects.all()
  user_requests=MembershipeRequesite.objects.all()
  discussion=Discussion.objects.all()
  sessions=ZoomMeeting.objects.filter(study_group=group, start_time__gte=datetime.now())
  attachments=Attachment.objects.all()

  return render(request,"main/group_dashboard.html" , {"users":users,"group":group , "members":members , "user_requests":user_requests , "discussion":discussion ,"sessions":sessions , "attachments":attachments} )


def user_dashboard(request:HttpRequest , user_id):
  user=User.objects.get(pk=user_id)
  user_requests=MembershipeRequesite.objects.filter(member=user_id)
  todo_list=ToDoList.objects.all

  return render(request,"main/user_dashboard.html" ,{"user":user , "user_requests":user_requests , "todo_list":todo_list })






def create_group(request:HttpRequest,user_id):
  user=User.objects.get(pk=user_id)
  if request.method =="POST":
    try:
     new_group=StudyGroup(
      creator=request.user,
      name=request.POST["name"],
      description=request.POST["description"],
      icon=request.FILES.get("icon" , default="images/default.jpg"),
            )
     new_group.save()
     new_member=MembershipeRequesite(
        group=new_group,
        member=request.user,
        status=request.POST.get("status" ,default="Accept"),
        )
     new_member.save()
    except Exception as e:
            print(e)
    return redirect('main:user_dashboard_view',user_id=user.id)

  return render(request,"main/create_group.html",{"user":user})



def admin_delete_group(request:HttpRequest , group_id):
  if request.user.is_superuser: 
    try:
      group=StudyGroup.objects.get(pk=group_id)
      group.delete()
    except StudyGroup.DoesNotExist:
      return redirect('main:not_allowed_view')
    except Exception as e:
      print(e)
    return redirect('main:admin_dashboard_view',request.user.id)
  



def creator_delete_group_view(request:HttpRequest , group_id):
  if StudyGroup.objects.filter(creator_id=request.user.id) or request.user.is_superuser: 
    try:
      group=StudyGroup.objects.get(pk=group_id)
      group.delete()
    except StudyGroup.DoesNotExist:
      return redirect('main:not_found_view')
    except Exception as e:
      print(e)
    return redirect('main:user_dashboard_view' , user_id=request.user.id)



def member_request_view(request:HttpRequest , group_id): 
  if StudyGroup.objects.filter(creator=request.user.id) or request.user.is_superuser:  
    group=StudyGroup.objects.get(id=group_id)
    if request.method =="POST":
      try:
        group_request=StudyGroup.objects.get(pk=group_id)

        email = request.POST.get("user_name")
        if User.objects.filter(username=email).exists():
          specific_member=User.objects.get(username=email)

          if MembershipeRequesite.objects.filter(member=specific_member , group=group).exists() :
            messages.error(request, "request already send to this user ")
            return redirect("main:group_dashboard_view" ,group_id=group_id,user_id=specific_member.id)
          
          membership=MembershipeRequesite(
                group=group_request,
                member=specific_member,
                status=request.POST.get("status" ,default="Pending"),
            )
          membership.save() 
          messages.success(request, "request sent successfully ")
          return redirect('main:group_dashboard_view', group_id=group_request.id , user_id=request.user.id)
        else:
          #send email as an invite
          if request.method == 'POST':
           subject = 'دعوة للانضمام إلى موقع دراسي'
           message = 'نود دعوتك للانضمام إلى موقعنا الدراسي الذي يقدم مجموعة متنوعة من الخدمات التعليمية والموارد القيمة للطلاب والمهتمين بالتعلم.'
           sender_email = settings.EMAIL_HOST_USER
           recipient_email = email

           send_mail(subject, message, sender_email, [recipient_email])
          
          messages.error(request, "User Not found. Invitation email is sent.")
          return  redirect("main:group_dashboard_view" ,group_id=group_id,user_id=request.user.id)
      except Exception as e:
              print(e)
              messages.error(request, "username not found ")
              return redirect("main:group_dashboard_view" ,group_id=group_id,user_id=request.user.id)
    else:
      return redirect('main:not_allowed_view')
    
      





def accept_reject_member_request_view(request:HttpRequest , user_id , request_id ):
   user=User.objects.get(id=user_id)
   user_requests=MembershipeRequesite.objects.get(pk=request_id)
   if request.method =="POST":
      try:
         new_status=user_requests.status=request.POST["status"]
         if new_status == "Accept":
          user_requests.save()
          return redirect('main:user_dashboard_view' ,user_id= user.id )
         elif new_status == "Reject":
            user_requests.delete()
            return redirect('main:user_dashboard_view' , user_id= user.id )
        
      except Exception as e:
            print(e)
   return redirect('main:user_dashboard_view',user_id=request.user.id)

def remove_member_view(request:HttpRequest , user_id , request_id ,group_id ):
   group=StudyGroup.objects.get(pk=group_id)
   user=User.objects.get(id=user_id)
   user_requests=MembershipeRequesite.objects.get(pk=request_id)
   if request.method =="POST":
      try:
         new_status=user_requests.status=request.POST["status"]
         if new_status == "Reject":
          user_requests.delete()
          return redirect('main:group_dashboard_view' ,user_id= user.id ,group_id=group.id )
      except Exception as e:
            print(e)
            messages.error(request, "Somthing went worng ")
   return redirect('main:group_dashboard_view' ,user_id= user.id ,group_id=group.id )



def discussion_view(request:HttpRequest , group_id):
  if request.method == "POST":
        member_msg=StudyGroup.objects.get(pk=group_id)
        msg=Discussion(
        group=member_msg,
        user=request.user,
        message=request.POST["message"],
        )
        msg.save()
  return redirect('main:group_dashboard_view' , group_id=member_msg.id ,user_id=request.user.id )


def edit_discussion_view(request:HttpRequest , group_id , msg_id):
  if request.method == "POST":
    member_msg=StudyGroup.objects.get(pk=group_id)
    msg=Discussion.objects.get(pk=msg_id)
    try:
      msg.message=request.POST["message"]
      msg.save()
    except Discussion.DoesNotExist:
      msg=None
      return redirect('main:not_found_view')
    except Exception as e:
      print(e)
    return redirect('main:group_dashboard_view' , group_id=member_msg.id ,user_id=request.user.id)


def delete_discussion_view(request:HttpRequest , group_id , msg_id):
  try:
    member_msg=StudyGroup.objects.get(pk=group_id)
    msg=Discussion.objects.get(pk=msg_id)
    msg.delete()
  except Discussion.DoesNotExist:
    msg=None
    return redirect('main:not_found_view')
  except Exception as e:
    print(e)
  return redirect('main:group_dashboard_view' , group_id=member_msg.id ,user_id=request.user.id)


def not_found_view(request:HttpRequest):
   return render(request,"main/not_found.html")


def not_allowed_view(request:HttpRequest):
   return render(request,"main/not_allowed.html")



def admin_dashboard_view(request:HttpRequest,user_id):
   user=User.objects.get(pk=user_id)
   all_group_admin=StudyGroup.objects.all
   todo_list=ToDoList.objects.all
   return render(request,"main/admin_dashboard.html",{"all_group_admin":all_group_admin ,"todo_list":todo_list})