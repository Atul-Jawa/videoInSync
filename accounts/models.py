from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    #username firstname lastname email password 
    image      = models.ImageField(upload_to='profile_img', default='profile_img/image.jpg' )
    desciption = models.TextField(null=True, blank=True) 


