from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from django.core import validators

# Create your models here.

DRINK_TYPES = (
    (1, 'soft_drinks'),
    (2, 'drinks'),
    (3, 'wines'),
    (4, 'beer'),
    (5, 'juice'),
)

WINE_COLORS= (
    (1, 'white'),
    (2, 'rose'),
    (3, 'red'),
)

WINE_SWEETNESS= (
    (1, 'dry'),
    (2, 'sweet'),
    (3, 'semi-sweet'),
    (4, 'semi-dry'),
)

DRINK_VOLUME = (
    (1, 'by the glass'),
    (2, 'bottle'),
    (3, 'decanter'),
    (4, 'beer'),
    (5, 'juice'),
)

class Dish(models.Model):
    dish_name = models.CharField(max_length=150, verbose_name='danie')
    price = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='cena')

    def __str__(self):
        return '{} {}'.format(self.dish_name, self.price)

    class Meta:
        verbose_name = 'danie'
        verbose_name_plural = 'dania'

class Ingridient(models.Model):
    ingridient_name = models.CharField(max_length=64, verbose_name='składnik')
    dish = models.ForeignKey(Dish, verbose_name='danie', primary_key = True)

    def __str__(self):
        return '{} {}'.format(self.ingridient_name, self.dish)

    class Meta:
        verbose_name = 'składnik'
        verbose_name_plural = 'składniki'

class Drinks(models.Model):
    drink_type = models.IntegerField(choices=DRINK_TYPES, null=True, verbose_name='napoje typ')
    drink_volume = models.IntegerField(choices=DRINK_VOLUME, null=True, verbose_name='objętość')
    wine_colors = models.IntegerField(choices=WINE_COLORS, null=True, verbose_name='kolor wina')
    wine_sweetness = models.IntegerField(choices=WINE_SWEETNESS, null=True, verbose_name='smak wina')
    drink_name = models.CharField(max_length=99, null=True,verbose_name='napoje nazwa' )
    price = models.DecimalField(max_digits=5, decimal_places=1, default= 0.00,verbose_name='cena')

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
        return '{} {}'.format(self.subject, self.content, self.date_added)

    class Meta:
        verbose_name = 'kontakt'
        verbose_name_plural = 'kontakty'

# class Order(models.Model):
#     dish_name = models.CharField(max_length=99, verbose_name='danie')
#     drink = models.CharField(max_length=99, verbose_name='napój')
#     date_added = models.DateTimeField(default=now, verbose_name='wysłane')
#
#     def __str__(self):
#         return '{} {}'.format(self.subject, self.content, self.date_added)
#
#     class Meta:
#         verbose_name = 'zamówienie'
#         verbose_name_plural = 'zamówienia'

class BookSeat(models.Model):
    date=models.DateTimeField(verbose_name='data rezerwacji')
    time=models.TimeField(verbose_name='godzina rezerwacji')
    guest_number=models.IntegerField(verbose_name='ilość gości')
    name_surname=models.CharField(max_length=60, verbose_name='imię, nazwisko')
    email=models.CharField(max_length=90, verbose_name='email')
    phone=models.CharField(max_length=15, verbose_name='numer telefonu')
    message=models.TextField(verbose_name="wiadomość")

    def __str__(self):
        return '{} {} {} {} {} {} {}'.format(self.date,
                                           self.time,
                                           self.guest_number,
                                           self.name_surname,
                                           self.email,
                                           self.phone,
                                           self.message
                                             )
    class Meta:
        verbose_name = 'rezerwacja'
        verbose_name_plural = 'rezerwacje'
