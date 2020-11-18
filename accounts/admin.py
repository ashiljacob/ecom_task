from django.contrib import admin
from .models import Customer,Order,OrderItem,Product
# Register your models here.




@admin.register(Product)
class Item(admin.ModelAdmin):
    list_display = ['name','price','image','digital']
     
admin.site.register(Customer,)
admin.site.register(Order)
admin.site.register(OrderItem)

## Custom admin page

class CustomAdmin(admin.AdminSite):
    site_header = 'Ecommerce Website Admin'
    site_title = 'Ecom Admin Portal'
    index_title = 'Welcome to Ecom'

custom_admin_site = CustomAdmin(name='custom_admin')
custom_admin_site.register(Product,Item)