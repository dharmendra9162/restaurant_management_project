from django.urls import path
from .views import *

urlpatterns = [
    path("menu/", menu_view, name="menu"),
    
]

