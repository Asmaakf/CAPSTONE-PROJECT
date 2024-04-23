from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Attachment
from main.models import StudyGroup


# Create your views here.
def all_attachment_view(request:HttpRequest , group_id):
    attachments= Attachment.objects.all()
    group=StudyGroup.objects.get(pk=group_id)
    return render(request, "main/attachment.html", {"attachments": attachments , "group":group} )


def add_attachment_view(request:HttpRequest,group_id):
    if request.method == 'POST':
        if request.user.is_authenticated:    
         try:
            group=StudyGroup.objects.get(pk=group_id)
            new_attachment = Attachment(
                title=request.POST["title"],  
                media=request.FILES.get("media"),  
                uploaded_by=request.user,
                group=group,
            )
            
            new_attachment.save()
            return redirect("main:all_attachment_view",group_id=group.id)# تعديل
         except Exception as e:
                    print(e)
   
    return render(request, "main/attachment.html")

def delete_attachment_view(request:HttpRequest,attachment_id):
  try:
    contact=Attachment.objects.get(pk=attachment_id)
    contact.delete()
  except Attachment.DoesNotExist:
     contact=None
  except Exception as e:
    print(e)
  return redirect("attachments:attachment_view")

def update_attachment_view(request:HttpRequest,attachment_id):
    attachment = Attachment.objects.get(pk=attachment_id)

    if request.method == "POST":
        try:
           attachment.title = request.POST["title"]
           attachment.media = request.FILES.get["media", attachment.media]
           attachment.group= request.POST["group"] #تعديل هي والي تحتها
           attachment.uploaded_by = request.POST["uploaded_by"]
         
           attachment.save()
           return redirect("attachments:update_attachment", attachment_id = attachment.id)
        except Exception as e:
            print(e)
    return render(request, 'attachments/attachment_update.html',{"attachment":attachment})