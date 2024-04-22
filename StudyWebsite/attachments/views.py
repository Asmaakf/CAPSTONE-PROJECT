from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Attachment

# Create your views here.
def attachment_view(request:HttpRequest):
    if request.method == 'POST':
        if request.user.is_authenticated:
         uploaded_by=request.user
        try:
            new_attachment = Attachment(
                title=request.POST["title"],  
                media=request.FILES.get("media"),  
                uploaded_by=uploaded_by,
                #group=request.POST["group"],
            )
            
            new_attachment.save()
            return redirect("attachment:attachment_view")# تعديل
        except Exception as e:
                    print(e)
    attachments= Attachment.objects.all()
    return render(request, "attachment/attachment.html", {"attachments": attachments})
