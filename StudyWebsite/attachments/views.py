from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Attachment
from main.models import StudyGroup


# Create your views here.
def all_attachment_view(request:HttpRequest , group_id):
    if request.user.is_authenticated:    
      try:
          group=StudyGroup.objects.get(pk=group_id)
          attachments=Attachment.objects.filter(group=group_id)

      except Exception as e:
          return render(request, "main/not_allowed.html") # no permission page
      
      return render(request, "main/attachment.html", {"attachments": attachments ,"group":group} )
    else:
      return render(request, "main/not_allowed.html") # no permission page



def add_attachment_view(request:HttpRequest,group_id):
  if request.user.is_authenticated:    
    if request.method == 'POST':
      try:
        group=StudyGroup.objects.get(pk=group_id)
        new_attachment = Attachment(
          title=request.POST["title"],  
          media=request.FILES.get("media"),  
          uploaded_by=request.user,
          group=group,
        )
        new_attachment.save()
        return redirect("attachments:all_attachment_view",group_id=group.id)# تعديل
      except Exception as e:
        return render(request, "main/not_allowed.html") # no permission page
    return render(request, "main/attachment.html")
  else:
    return render(request, "main/not_allowed.html") # no permission page


def delete_attachment_view(request: HttpRequest, attachment_id, group_id):
    try:
        attachment = Attachment.objects.get(pk=attachment_id)
        group = StudyGroup.objects.get(pk=group_id)

        attachment.delete()
        return redirect("attachments:all_attachment_view", group_id=group.id)
       
    except Attachment.DoesNotExist:
        return render(request, "main/not_found.html")
    except Exception as e:
        print(e)
        # Handle other exceptions if necessary




def update_attachment_view(request: HttpRequest, attachment_id, group_id):
    group = StudyGroup.objects.get(pk=group_id)
    attachment = Attachment.objects.get(pk=attachment_id)

   
    
    if request.method == "POST":
       try:
         attachment.title = request.POST["title"]
         attachment.media = request.FILES.get("media", attachment.media)
         attachment.save()
         return redirect("attachments:all_attachment_view", group_id=group.id)
       except Exception as e:
                print(e)
    return render(request, 'main/attachment.html', {"attachment": attachment, "group": group})
   