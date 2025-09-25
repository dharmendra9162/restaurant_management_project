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

from django.urls import path 
from  . import views

urlpatterns =[
    path("", views.home, name="home"),
    path("about/", view.about, name="about"),
]

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import view

urlpatterns =[
    path("", views.home, name="home"),
]

if settings.DEBUG
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    from django.urls import path
    from .views import MenuCategoryListView

    urlpatterns = [
        path('menu_catgories/', MenuCategoryListView.as_view(), name='menu-categories'),
    ]

