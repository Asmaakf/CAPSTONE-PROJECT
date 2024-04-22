from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class StudyGroup(models.Model):
    creator=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length = 64)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    icon=models.ImageField(upload_to="images/", default="images/default.jpg")

