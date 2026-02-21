from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class customuser(AbstractUser):
    
    User_type=[
        ('admin','admin'),
        ('customer','customer'),
        ('seller','seller'),
    ]
    fullname=models.CharField(choices=User_type, max_length=50,null=True)
    user_type=models.CharField(null=True, max_length=50)
    
    