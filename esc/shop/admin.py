from django.contrib import admin

# Register your models here.

from .models import Product,Register

admin.site.register(Product)
admin.site.register(Register)