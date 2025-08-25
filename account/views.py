from rest_framework.decorators import api_view
from rest_framework.response import response

@api_view['GET']
def get_menu(request):
    menu =[
        {
            "name":"Margherita Pizza"
            "description":"classic Pizza with tomato sauce, and basil",
            "Price":10.30
        },
        {
            "name":"pasta Alfredo",
            "description": "creamy Alfredo sauce with fettuccicine pasta",
            "price":10.40
        }
    ]
    return response(menu)


from django.conf import settings
from django.shortcuts import render


def home (request):
    restaurant_name = getattr(settings,"RESTAURANT_NAME","my Restaurant")
    return render(request,"home.html",{"restaurant_name": restaurant_name})
    

from django.conf import settings
from django.shortcuts import render

def home_view(request)
    return render(
        request,
        'home.html',
        {
            'restaurant_name': 'Spice Garden',
            'phone_number': settings.RESTAURANT_PHONE
        }
    )