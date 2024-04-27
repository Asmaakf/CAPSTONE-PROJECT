from django.urls import path
from . import views

app_name  = "common_questions"

urlpatterns = [
    path('support_question_answer/', views.support_question_answer, name='support_question_answer'),  
    path('view-messages/', views.view_messages, name='view_messages'),  
    path('delete_question/<int:pk>/', views.delete_question, name='delete_question'),  
    path('edit_question/<int:pk>/', views.edit_question, name='edit_question'),  
]