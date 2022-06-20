from django.db import models

from car.models import Car


class Order(models.Model):
    name = models.CharField(max_length=255, default='unknown')
    email = models.EmailField(default='unknown')
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100, default='unknown')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='cars')

    class Meta:
        db_table = 'order'
