from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Menu (models.Model):
    name = Menu(models.Model):
    description = models.CharField(max_lenght=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

class order(models.Model):
    STATUS_CHOICES = [
        ('PENDING','pending'),
        ('PROCESSING','processing'),
        ('COMPLETED','completed'),
        ('CANCELLED','Cancelled')
    ]
    customer = models.Foreignkey(User,on_delete=models.CASCADE, related_name='item')
    menu_item = models.Foreignkey(menu,on_delete=models.CASCADE)
    quantity = models.positiveIntegerField()

    def __str__(self):
        return f"{self.menu_item.name}(x{self.quantity})"

    def get_total_price(self):
        return self.quantity *self.menu_item.price    