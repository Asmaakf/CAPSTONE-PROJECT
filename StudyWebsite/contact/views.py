from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import ContactSupport
from django.contrib.auth.models import User

# Create your views here.

def contact_view(request:HttpRequest):
    if request.method == 'POST':
        try:
          
            new_con = ContactSupport(
                name=request.POST['name'],  
                email=request.POST["email"], 
                message= request.POST["message"]
            )
            
            new_con.save()
            return redirect("main:index_view")
        except Exception as e:
                    print(e)
        

    return render(request, "contact/contact.html")


def message_view(request:HttpRequest):
 if not request.user.is_superuser:
        return redirect(request, "main/not_found.html")
 contacts = ContactSupport.objects.all()
 return render(request, "contact/message.html", {"contacts" : contacts })


def delete_message(request:HttpRequest ,msg_id):
  
  if not request.user.is_superuser:
    return redirect('main:not_allowed_page') #باقي مو موجوده
  try:
    contact=ContactSupport.objects.get(pk=msg_id)
    contact.delete()
  except ContactSupport.DoesNotExist:
     contact=None
  except Exception as e:
    print(e)

    
  return redirect('contact:message_view')