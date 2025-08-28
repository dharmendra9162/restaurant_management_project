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
 from django.shortcuts import render
 from .models import RestaurantInfo

def home_view(request):
    restaurant = RestaurantInfo.objects.first()
    return render(
        request,
        'home.html',
        {
            'restaurant_name': restaurant_name if restaurant else "our Restaurant",
            'phon_number': restaurent.phone if restaurant else "N/A"
        }
    )    

    from django.shortcuts import render

    def contact_view(request):
        return render(request,'contact .html')
from  django.shortcuts import render

def menu_view(request):
    #Hardcoded list of menu items(later replace with DB)
    menu_items = [
        {"name": "paner Butter Masala","price": 250,"category": "Main Course"},
        {"name": "Veg Biryani", "Price": 200, "Category": "Rice"},
        {"name": "Tandoori Roti","price":25, "category":"Bread"},
        {"name": "Gulab Jamun", "price":80, "category": "Dessert"},

    ]

    return render(request, "menu.html", {"menu_items": menu_items})



    from datetime import datetime
    def home_view(request):
        return render(request,"home.html", {
            "restaurant_name": "Spice Garden",
            "year": datetime.now().year
        })

def menu_view(request)
    try:
        # Later this will fetch from the database
        menu_items = [
            {"name": "panner Butter masala", "price":250, "category": "Main Course"},
            {"name": " Veg Biryani", "price":200, "category": "Rice"},
            {"name": "Tandoori Roti", "price":25, "category": "Bread"}
        ]
    except DatabaseError:
        # Handle DB error gracefully
        menu_items = []
        error_message = "sorry, We're having trouble loading  the menu right now."
        return render(request, "menu.html", {"menu_items": menu_items, "error": error_message})

    return render(request, "menu.html",{"menu_iteam"})    


def home_view(request):
    return render(request,"home.html", {"current_year". datetime.now().year})
                    