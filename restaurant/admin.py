from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Drinks)
class DrinksAdmin(admin.ModelAdmin):
    list_display = ['drink_type', 'drink_volume', 'wine_colors', 'wine_sweetness', 'drink_name', 'price']

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['dish_name', 'price']

@admin.register(Ingridient)
class IngridientAdmin(admin.ModelAdmin):
    list_display = ['ingridient_name', 'dish']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['subject', 'content', 'contact_details', 'email', 'phone_number']
    exclude = ['date_added']

@admin.register(BookSeat)
class BookSeatAdmin(admin.ModelAdmin):
    list_display = ['date', 'time', 'guest_number', 'name_surname', 'email', 'phone', 'message']
