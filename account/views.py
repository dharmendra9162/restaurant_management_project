from django.shortcuts import render

# Create your views here.
import requests 
from django.shortcuts import render

def menu_home (request):
    response = requests('http://localhost:8000/api/menu/')
    if response.status_code == 200:
        menu_items = response.json()
    else:
        menu_items = []
    return render(request,'menu.html',{'menu_items':menu_items})    
