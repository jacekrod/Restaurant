from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views import View


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
        return render(request, 'menu.html', {'dishes': dishes,
                                             'drinks': drinks,
                                             'wines': wines,
                                             'beers': beers,
                                             'juices': juices,
                                             'soft_drinks': soft_drinks
                                             })


class OrderView(View):

    def post(self, request):
        form = OrderForm(request.POST)
        if form.is_valid():
            new = Order.objects.create(
                                       # dish_name=request.POST.get('dish_{{dish.id}}'),
                                       # drink=request.POST.get('drink_{{drink.id}}'),
                                       name_surname=request.POST.get('name_surname'),
                                       address=request.POST.get('address'),
                                       email=request.POST.get('email'),
                                       phone_number=request.POST.get('phone_number'),
                                       self_pickup=request.POST.get('self_pickup')
                                       # dish_order_quantity=request.POST.get('dish_order_quantity'),
                                       # wine_order_quantity=request.POST.get('wine_order_quantity'),
                                       # drink_order_quantity=request.POST.get('drink_order_quantity'),
                                       # juice_order_quantity=request.POST.get('juice_order_quantity'),
                                       # beer_order_quantity=request.POST.get('beer_order_quantity'),
                                       )
        # print(request.POST.keys())
        # print(request.POST)
        # keys = ' '.join(request.POST.keys())
        # print(keys)  # to mój komentarz
        for e in request.POST.keys():
            print(e, request.POST.get(e))
        return redirect('order')

    def get(self, request):
        form = OrderForm
        dishes = Dish.objects.all()
        wines = Drinks.objects.filter(drink_type=3)
        beers = Drinks.objects.filter(drink_type=4)
        juices = Drinks.objects.filter(drink_type=5)
        soft_drinks = Drinks.objects.filter(drink_type=1)
        drinks = Drinks.objects.filter(drink_type=2)
        # for e in drinks:
        #     print (vars(e))
        # print(len(dishes), len(wines), len(beers), juices, soft_drinks , drinks)
        return render(request, 'order.html', {'dishes': dishes,
                                              'drinks': drinks,
                                              'wines': wines,
                                              'beers': beers,
                                              'juices': juices,
                                              'soft_drinks': soft_drinks,
                                              'form': form})


class BookSeatView(View):
    def get(self, request):
        form = BookSeatForm
        return render(request, 'book_a_seat.html', {'form': form})

    def post(self, request):
        form = BookSeatForm(request.POST)
        if form.is_valid():
            new = BookSeat.objects.create(date=request.POST.get('date'),
                                          time=request.POST.get('time'),
                                          guest_number=request.POST.get('guest_number'),
                                          name_surname=request.POST.get('name_surname'),
                                          email=request.POST.get('email'),
                                          phone=request.POST.get('phone'),
                                          message=request.POST.get('message')
                                          )
        return redirect('book')


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')


class ContactView(View):
    def get(self, request):
        form = ContactForm
        return render(request, 'contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            new = Contact.objects.create(subject=request.POST.get('subject'),
                                         content=request.POST.get('content'),
                                         contact_details=request.POST.get('contact_details'),
                                         email=request.POST.get('email'),
                                         phone_number=request.POST.get('phone_number')
                                         )
            return redirect('contact')

            # class OrderView(View):
            #     def get(self, request):
            #         # form = OrderForm
            #         dishes = Dish.objects.all()
            #         wines = Drinks.objects.filter(drink_type=3)
            #         beers = Drinks.objects.filter(drink_type=4)
            #         juices = Drinks.objects.filter(drink_type=5)
            #         soft_drinks = Drinks.objects.filter(drink_type=1)
            #         drinks = Drinks.objects.filter(drink_type=2)
            #         return render(request, 'order.html', {'dishes': dishes,
            #                                              'drinks': drinks,
            #                                              'wines': wines,
            #                                              'beers': beers,
            #                                              'juices': juices,
            #                                              'soft_drinks': soft_drinks
            #                                              })


# class DishView(View):
#     def get(self, request):
#         form = DishForm
#         return render(request, 'form.html', {'form': form})
#     def post(self, request):
#         form = DishForm(request.POST)
#         if form.is_valid():
#             new = Dish.objects.create(dish_name = request.POST.get('dish_name'),
#                                       price = request.POST.get('price'),
#                                       ingredient = request.POST.get('ingredient'))
#         return redirect ('dish')
# #
# class IngredientView(View):
#     def get(self, request):
#         form = IngredientForm
#         return render(request, 'form.html', {'form': form})
#     def post(self, request):
#         form = IngredientForm(request.POST)
#         if form.is_valid():
#             new = Ingredient.objects.create(ingredient_name = request.POST.get('ingredient_name'))
#             dish_id = new.dish_id
#         return redirect ('ingredient')
#
# class DrinksView(View):
#     def get(self, request):
#         form = DrinksForm
#         return render(request, 'form.html', {'form': form})
#     def post(self, request):
#         form = DrinksForm(request.POST)
#         if form.is_valid():
#             new = Drinks.objects.create(drink_type = request.POST.get('drink_type'),
#                                         drink_volume = request.POST.get('drink_volume'),
#                                         wine_colors = request.POST.get('wine_colors'),
#                                         wine_sweetness = request.POST.get('wine_sweetness'),
#                                         drink_name = request.POST.get('drink_name'),
#                                         price=request.POST.get('price')
#                                         )
#         return redirect ('drinks')

