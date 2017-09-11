from django.forms import ModelForm
from .models import *


class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = "__all__"


class IngridientForm(ModelForm):
    class Meta:
        model = Ingridient
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
        model = Contact
        fields = "__all__"

class BookSeatForm(ModelForm):
    class Meta:
        model = BookSeat
        fields = "__all__"