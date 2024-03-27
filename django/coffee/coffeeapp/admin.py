from django.contrib import admin
from .models import Coffee  # Corrected model name to uppercase 'Coffee'

class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')  # Specifies which fields to display in the admin list view

admin.site.register(Coffee, CoffeeAdmin)  # Registers the Coffee model with its corresponding admin class
