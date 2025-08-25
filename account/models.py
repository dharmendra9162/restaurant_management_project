from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.oneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    phone_number = models.CharField(max_length=15,blank=True)
    
    def __str__(self):
        return self.username

from django.db import models

class RestaurantInfo(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name