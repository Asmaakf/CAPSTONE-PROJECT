from django.db import models
from django.contrib.auth.models import User
#from main.models import studygroup
# Create your models here.

class Attachment(models.Model):
    title= models.CharField(max_length=2000)
    media=models.FileField(upload_to="attachments")
    uploaded_by=models.ForeignKey(User,on_delete=models.CASCADE)
    uploaded_at=models.DateTimeField(auto_now_add=True)
