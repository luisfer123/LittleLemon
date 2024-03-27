from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length = 255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateField()
    
    def __str__(self) -> str:
        return f'{self.name} for {self.no_of_guests} guests on {self.booking_date}'
    
class Menu(models.Model):
    title = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
    inventory = models.IntegerField(default = 0)
    
    def __str__(self) -> str:
        return f'{self.title} : {str(self.price)}'