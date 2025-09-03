from django.urls import path
from .views import get_menu

urlpatterns = [
    path('api/menu/',get_menu,name='get_menu')
]


from django.urls import path
from .views import home 

urlpatterns=[
    path("", home, name="home")
]


