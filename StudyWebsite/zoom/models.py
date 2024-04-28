from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User  
from main.models import StudyGroup

class ZoomMeeting(models.Model):
    topic = models.CharField(max_length=100)
    agenda = models.CharField(max_length=200, blank=True, null=True)  
    start_time = models.DateTimeField()  
    password = models.CharField(max_length=10, blank=True, null=True) 
    timezone = models.CharField(max_length=50, default="Asia/Riyadh")
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    study_group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE)
    start_url = models.URLField(blank=True, null=True)  
    join_url = models.URLField(blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True) 
    

    def __str__(self):
        return f"{self.topic} - {self.start_time}"

