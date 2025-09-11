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


urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls imort path
from . import views

urlpatterns = [
    path('contact/',view.contact_view, name='contact')
]

from django.urls imort path
from . import views

urlpatterns =[
    path('',views.home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)