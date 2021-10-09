from django.contrib import admin
from .models import *

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']
    list_per_page = 10
    search_fields = ['name']
admin.site.register(Customer)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_per_page = 10
    search_fields = ['name', 'price']
admin.site.register(Product)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['status']
    list_per_page = 10
    search_fields = ['status']
admin.site.register(Order)

admin.site.register(Tag)
