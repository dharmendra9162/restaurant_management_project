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

class MenuItm(models.model):
    name = model.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.decimalFiel(max_digits=6, decimal_place=2)

    def __str__(self):
        return self.name   


class Contact(models.model):
    name = models.CharField(max_length=100)
    email = model.EmailField()             


    class Restaurant(models.model):
        name = models.CharField(max_length=100)
        address = models.TextField()

        def __str__
        return self.name
from django.db import models
class ContactSubmission(model.models)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    submitted_at = models.DateTimeField(auto_now_add=Truee)

    def __str__(self):
        return f"{self.name} - {self.email}"  


from django import froms
from .model import ContactSubmission

class ContactFrom(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email']


from django.db import models

class RestaurantLocation(models.model):
    address = models.CharField(max_length=225)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code =models.CharField(max_length=20)

    def __str__(self):
        ret f"{self.addres}, {self.city}, {self.sate} {self.zip_code}"
