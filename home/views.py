from django.shortcuts import render

# Create your views here.
def menu_view(request):
    items = MenuItem.objects.all()
    return render(request,"menu.html",{"items": items})