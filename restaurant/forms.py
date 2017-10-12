from django.forms import ModelForm
from .models import *
from django import forms


class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = "__all__"



class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"


class DrinksForm(ModelForm):
    class Meta:
        model = Drinks
        fields = "__all__"

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        exclude = ['date_added']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ['dish', 'drink', 'date_added', 'dish_order_quantity', 'wine_order_quantity', 'juice_order_quantity', 'beer_order_quantity', 'drink_order_quantity']


class BookSeatForm(ModelForm):
    class Meta:
        model = BookSeat
        fields = "__all__"
        widgets = {
            'date': forms.TextInput(attrs={'placeholder': 'RRRR-MM-DD'}),
            'time': forms.TextInput(attrs={'placeholder': 'GG:MM'})

        }