from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import ToDoList
from django.contrib.auth.models import User
# Create your views here.

def add_todo_view(request:HttpRequest,user_id):

    if request.method == 'POST':
        if request.user.is_authenticated:    
         try:
            user=User.objects.get(pk=user_id)
            new_todo =ToDoList(
                user=user,  
                todo=request.POST["todo"],
                checked=request.POST.get(default=False),
            )
            new_todo.save()
            return redirect("todo_list:all_todo_view",user_id=user.id)# تعديل
         except Exception as e:
                    print(e)
   
    return render(request, "todo_list/todo.html")

def all_todo_view(request:HttpRequest,user_id):
     user=User.objects.get(pk=user_id)
     todo= ToDoList.objects.filter(user=user)
     return render(request, "todo_list/todo.html", {"todo":todo ,"user":user} )

def delete_todo_view(request:HttpRequest,todo_id,user_id):
  user=User.objects.get(pk=user_id)
  try:
    todo=ToDoList.objects.get(pk=todo_id)
    todo.delete()
  except ToDoList.DoesNotExist:
     todo=None
  except Exception as e:
    print(e)
  return redirect("todo_list:all_todo_view",user_id=user.id)

def update_todo_view(request:HttpRequest,todo_id,user_id):
    user=User.objects.get(pk=user_id)
    todo=ToDoList.objects.get(pk=todo_id)

    if request.method == "POST":
        try:
           todo.todo = request.POST["todo"]
           todo.checked=request.POST["checked"]
           todo.save()
           return redirect("todo_list:all_todo_view",user_id=user.id)
        except Exception as e:
            print(e)
    return render(request, 'todo_list/todo.html',{"todo":todo,"user":user})