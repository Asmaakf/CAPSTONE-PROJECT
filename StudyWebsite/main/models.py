from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class StudyGroup(models.Model):
    creator=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length = 64)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    icon=models.ImageField(upload_to="images/", default="images/default.jpg")



class MembershipeRequesite(models.Model):
    status_choice = models.TextChoices("Status", ["Accept","Reject","Pending"])
    
    group=models.ForeignKey(StudyGroup,on_delete=models.CASCADE)
    member=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length = 64 , choices=status_choice.choices , default="Pending")
    date_joined=models.DateTimeField(auto_now_add=True)



class Discussion(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    group=models.ForeignKey(StudyGroup,on_delete=models.CASCADE)
    message=models.TextField()
    msg_at=models.DateTimeField(auto_now_add=True)
