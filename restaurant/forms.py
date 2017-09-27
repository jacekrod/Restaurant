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
        fields = "__all__"


class BookSeatForm(ModelForm):
    class Meta:
        model = BookSeat
        fields = "__all__"