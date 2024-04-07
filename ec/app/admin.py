from django.contrib import admin
from .models import Customer, Product, Cart

# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display= ['id', 'title', 'discounted_price','category', 'product_image']



@admin.register(Customer)
class ProductModelAdmin(admin.ModelAdmin):
    list_display= ['id', 'user','city', 'locality' ,'state', 'zipcode']



class CartModelAdmin(admin.ModelAdmin):
    list_display=['id', 'user', 'product', 'quantity']

admin.site.register(Cart, CartModelAdmin)

