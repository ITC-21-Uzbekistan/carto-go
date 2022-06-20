from django.db import models

from car.models import Car


class Order(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='cars')

    class Meta:
        db_table = 'order'
