from django.contrib import admin
from .models import *


# Register your models here
class Product_Category_Admin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    ordering = ['id']
    prepopulated_fields = {'slug': ('name',)}


class Manufacturer_Admin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    ordering = ['id']
    prepopulated_fields = {'slug': ('name',)}




class Product_Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'discount', 'final_price', 'cat', 'mnf']
    list_display_links = ['id', 'name']
    ordering = ['id']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['price', 'discount']
    list_filter = ['cat', 'mnf']


admin.site.register(Product_Category, Product_Category_Admin)
admin.site.register(Manufacturer, Manufacturer_Admin)
admin.site.register(Product, Product_Admin)
