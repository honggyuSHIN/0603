from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    REQUIRED_FIELDS=[]
    email=None
    nickname=models.CharField(max_length=100)
    university=models.CharField(max_length=50)
    location=models.CharField(max_length=200)