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
                    

def home_view(request):
    return render(request, "home.html", {
        "restaurant_name": settings.RESTAURANT_NAME,
        "current_year": datetime.now().year

    })


    def home(request):
        if request.method == 'POST'
        from = contactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else
            form = contactForm()
            return render(request,"home.html",{"form":form})
            
    def home(request):
        restaurent = Restaurant.objects.first()
        return render(request,'home.html',{'restaurant': restaurent})            


    def menu_view(request):
        menu_iteam = MenuItems.objects.all()
        return render(request, 'menu.html', {'menu_items': menu_iteam})


from django.shortcuts import render, redirect
from.forms import contactForm

def contact_view(request):
    if request.method == "POST":
        from = contactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contat')
    else:
        form = contactForm()
    return render(request, 'contact.html', {'form': form})            

form django.shortcuts import render
from .models import MenuItems

def home_view(request):
    query = request.GET('q', '')
    if query:
        menu_items = MenuItems.objects.filter(name__icotains=query)
else:
    menu_items = MenuItems.objects.all()
    return render(request, 'home.html', {'menu_items': menu_iteam, 'query':query})        


from django.shortcuts import render
from django .core.mail import send_mail
from django.conf.import settings
from.form import contactForm

def contact_view(request):
    if request.method=="POST":
        form = contactForm(request.POST)
        if form.is_valid():
            send_mail(
                f"Message from {form.cleaned_data['name]},
                form.cleaned_data['message'],
                form.cleaned_data['email'],
                [settings.EMAIL_HOST_USER]
            )
            return render(request, "contact.html", {"form": form, "success": True})

    else:
        form = contactForm()
        return render(request,"contact.html",{"form: form})


from django.shortcuts import render
from .models import Restaurant

def home(request):
restaurant = Restaurant.objects.first()
return render(request, "home.html", {"restaurent": restaurant})

from django.shortcuts import render
from .models import Restaurant

def home(request):
    restaurent = Restaurant.objects.first()
    return render(request,"home.html", {"restaurent":restaurant})

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import contactForm

def contact_view(request):
    success = False
    if request.method == "POST"
    if form.is_valid():
        # Data is alredy validated
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        subject = f"New contact Message from {name}"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        send_mail(subject,body,settings.DEFAULT_FORM_EMAIL,[settings.EMAIL_HOST_USER])
    else:
        from = contactForm()
        return render(request,"contact.html",{"form": form , "success": success})
                
from django.shortcuts import redirect

def add_to_cart(request, item_id):
    cart  = request.session.get("cart", {})
    cart[item_id] = cart.get(item_id, 0) +1
    request.session["cart"] = cart
    return redirect("home")
    from django.shortcuts import render

    def home(request):
        cart = request.session.get("cart", {})
        cart_count = sum(cart.values())
        return render(request, "home.html",{"cart_count: cart_count"})
 
 from django.shortcuts import render

 def about (request):
    return render(request, "about.html")