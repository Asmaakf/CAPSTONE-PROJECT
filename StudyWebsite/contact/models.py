from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ContactSupport(models.Model):
    name=models.CharField(max_length=64)
    message=models.TextField()
    email=models.EmailField()
    msg_at=models.DateTimeField(auto_now_add=True)
