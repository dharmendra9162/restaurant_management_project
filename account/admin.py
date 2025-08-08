from django.contrib import admin
from .models import menu , order  

class  MenuAdmin(admin.ModelAdmin):
    list_display = ('name','price','category','is_available')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name','menu_item','quantity','order_date','status',)


admin.site.register(Menu,MenuAdmin)
admin.site.register(Order,OrderAdmin)