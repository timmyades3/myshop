from django.contrib import admin
from .models import Product,Offer

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

admin.site.register(Product, ProductsAdmin)

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')

admin.site.register(Offer,OfferAdmin)
