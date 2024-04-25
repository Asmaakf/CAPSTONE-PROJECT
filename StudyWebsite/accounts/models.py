from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar/', default="images/default_img.jpg")
    bio = models.TextField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    linkedin_link = models.CharField(max_length=100, blank=True, null=True)
    github_link = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

