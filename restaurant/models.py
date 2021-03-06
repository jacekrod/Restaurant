from django.db import models
from django.utils.timezone import now
from django.core import validators

# Create your models here.

DRINK_TYPES = (
    (1, 'soft_drinks'),
    (2, 'drinks'),
    (3, 'wines'),
    (4, 'beer'),
    (5, 'juice'),
)

WINE_COLORS = (
    (1, 'white'),
    (2, 'rose'),
    (3, 'red'),
)

WINE_SWEETNESS = (
    (1, 'dry'),
    (2, 'sweet'),
    (3, 'semi-sweet'),
    (4, 'semi-dry'),
)

DRINK_VOLUME = (
    (1, 'by the glass'),
    (2, 'bottle'),
    (3, 'decanter'),
)


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=64, verbose_name='składnik')

    def __str__(self):
        return '{}'.format(self.ingredient_name)

    class Meta:
        verbose_name = 'składnik'
        verbose_name_plural = 'składniki'


class Dish(models.Model):
    dish_name = models.CharField(max_length=150, verbose_name='danie')
    price = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='cena')
    ingredient = models.ForeignKey(Ingredient)

    def __str__(self):
        return '{} {} {}'.format(self.dish_name, self.price, self.ingredient)

    class Meta:
        verbose_name = 'danie'
        verbose_name_plural = 'dania'


class Drinks(models.Model):
    drink_type = models.IntegerField(choices=DRINK_TYPES, null=True, blank=True, verbose_name='napoje typ')
    drink_volume = models.IntegerField(choices=DRINK_VOLUME, null=True, blank=True, verbose_name='objętość')
    wine_colors = models.IntegerField(choices=WINE_COLORS, null=True, blank=True, verbose_name='kolor wina')
    wine_sweetness = models.IntegerField(choices=WINE_SWEETNESS, null=True, blank=True, verbose_name='smak wina')
    drink_name = models.CharField(max_length=99, null=True, blank=True, verbose_name='napoje nazwa')
    price = models.DecimalField(max_digits=5, decimal_places=1, default=0.00, verbose_name='cena')

    def __str__(self):
        return '{} {} {} {} {} {} '.format(self.drink_type,
                                           self.drink_volume,
                                           self.wine_colors,
                                           self.wine_sweetness,
                                           self.drink_name,
                                           self.price)

    class Meta:
        verbose_name = 'napój'
        verbose_name_plural = 'napoje'


class Contact(models.Model):
    contact_details = models.CharField(max_length=99, null=True, verbose_name='Imię i nazwisko')
    email = models.EmailField(validators=[validators.EmailValidator], blank=True)
    phone_number = models.CharField(max_length=12, null=True, verbose_name='numer telefonu')
    subject = models.CharField(max_length=99, verbose_name='temat')
    content = models.TextField(verbose_name='treść')
    date_added = models.DateTimeField(default=now, verbose_name='wysłane')

    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.contact_details,
                                          self.email,
                                          self.phone_number,
                                          self.subject,
                                          self.content,
                                          self.date_added
                                          )

    class Meta:
        verbose_name = 'kontakt'
        verbose_name_plural = 'kontakty'


class Order(models.Model):
    name_surname = models.CharField(max_length=99, verbose_name='imię nazwisko')
    address = models.CharField(max_length=199, verbose_name='adres')
    email = models.EmailField(verbose_name='email')
    phone_number = models.CharField(max_length=20, verbose_name='numer telefonu')
    self_pickup = models.BooleanField(verbose_name='odbiór własny')
    dish = models.ManyToManyField(Dish, verbose_name='danie')
    drink = models.ManyToManyField(Drinks, verbose_name='napój')
    date_added = models.DateTimeField(default=now, verbose_name='wysłane')
    dish_order_quantity = models.CharField(max_length=10, verbose_name=' danie główne ilość', default=0)
    drink_order_quantity = models.CharField(max_length=10, verbose_name='drink ilość', default=0)
    wine_order_quantity = models.CharField(max_length=10, verbose_name='wino ilość', default=0)
    juice_order_quantity = models.CharField(max_length=10, verbose_name='sok ilość', default=0)
    beer_order_quantity = models.CharField(max_length=10, verbose_name='piwo ilość', default=0)

    def __str__(self):
        return '{} {} {} {} {} {} {} {} {} {} {} {}'.format(self.name_surname,
                                                               self.address,
                                                               self.email,
                                                               self.phone_number,
                                                               self.self_pickup,
                                                               # self.dish,
                                                               self.drink,
                                                               self.date_added,
                                                               self.dish_order_quantity,
                                                               self.drink_order_quantity,
                                                               self.wine_order_quantity,
                                                               self.juice_order_quantity,
                                                               self.beer_order_quantity,
                                                               )

    class Meta:
        verbose_name = 'zamówienie'
        verbose_name_plural = 'zamówienia'


class BookSeat(models.Model):
    date = models.DateTimeField(verbose_name='data rezerwacji')
    time = models.TimeField(verbose_name='godzina rezerwacji')
    guest_number = models.IntegerField(verbose_name='ilość gości')
    name_surname = models.CharField(max_length=60, verbose_name='imię, nazwisko')
    email = models.CharField(max_length=90, verbose_name='email')
    phone = models.CharField(max_length=15, verbose_name='numer telefonu')
    message = models.TextField(verbose_name="wiadomość")

    def __str__(self):
        return '{} {} {} {} {} {} {}'.format(self.date,
                                             self.time,
                                             self.guest_number,
                                             self.name_surname,
                                             self.email,
                                             self.phone,
                                             self.message)

    class Meta:
        verbose_name = 'rezerwacja'
        verbose_name_plural = 'rezerwacje'
