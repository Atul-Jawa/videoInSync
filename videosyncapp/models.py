from django.db import models
from accounts.models import User

# Create your models here.
class Group(models.Model):
    group_name  = models.CharField(max_length=100)
    admin       = models.ForeignKey(User, verbose_name='admin', on_delete= models.CASCADE)