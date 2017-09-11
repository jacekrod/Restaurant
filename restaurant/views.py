from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views import View
from django.http import HttpResponse

# Create your views here.


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class MenuView(View):
    def get(self, request):
        dishes = Dish.objects.all()
        wines = Drinks.objects.filter(drink_type=3)
        beers = Drinks.objects.filter(drink_type=4)
        juices = Drinks.objects.filter(drink_type=5)
        soft_drinks = Drinks.objects.filter(drink_type=1)
        drinks = Drinks.objects.filter(drink_type=2)
        return render(request, 'menu.html', {'dishes':dishes,
                                             'drinks':drinks,
                                             'wines':wines,
                                             'beers':beers,
                                             'juices':juices,
                                             'soft_drinks':soft_drinks
                                             })


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')


class ContactView(View):
    def get(self, request):
        form = ContactForm
        return render(request, 'contact.html', {'form':form})
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            new = Contact.objects.create(subject = request.POST.get('subject'),
                                         content = request.POST.get('content'),
                                         contact_details=request.POST.get('contact_details'),
                                         email=request.POST.get('email'),
                                         phone_number = request.POST.get('phone_number')
                                         )
            return redirect('contact')

class OrderView(View):
    def get(self, request):
        form = OrderForm
        return render(request, 'order.html', {'form':form})


class DishView(View):
    def get(self, request):
        form = DishForm
        return render(request, 'form.html', {'form': form})
    def post(self, request):
        form = DishForm(request.POST)
        if form.is_valid():
            new = Dish.objects.create(dish_name = request.POST.get('dish_name'),
                                      price = request.POST.get('price'))
        return redirect ('dish')
#
class IngridientView(View):
    def get(self, request):
        form = IngridientForm
        return render(request, 'form.html', {'form': form})
    def post(self, request):
        form = IngridientForm(request.POST)
        if form.is_valid():
            new = Ingridient.objects.create(ingridient_name = request.POST.get('ingridient_name'))
            dish_id = new.dish_id
        return redirect ('ingridient')

class DrinksView(View):
    def get(self, request):
        form = DrinksForm
        return render(request, 'form.html', {'form': form})
    def post(self, request):
        form = DrinksForm(request.POST)
        if form.is_valid():
            new = Drinks.objects.create(drink_type = request.POST.get('drink_type'),
                                        drink_volume = request.POST.get('drink_volume'),
                                        wine_colors = request.POST.get('wine_colors'),
                                        wine_sweetness = request.POST.get('wine_sweetness'),
                                        drink_name = request.POST.get('drink_name'),
                                        price=request.POST.get('price')
                                        )
        return redirect ('drinks')

class BookSeatView(View):
    def get(self, request):
        form = BookSeatForm
        return render(request, 'book_a_seat.html', {'form': form})
    # def post(self, request):
    #     form = DrinksForm(request.POST)
    #     if form.is_valid():
    #         new = Drinks.objects.create(drink_type = request.POST.get('drink_type'),
    #                                     drink_volume = request.POST.get('drink_volume'),
    #                                     wine_colors = request.POST.get('wine_colors'),
    #                                     wine_sweetness = request.POST.get('wine_sweetness'),
    #                                     drink_name = request.POST.get('drink_name'),
    #                                     price=request.POST.get('price')
    #                                     )