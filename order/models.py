from django.db import models

from car.models import Car


class Order(models.Model):
    name = models.CharField(max_length=255, default=None)
    email = models.EmailField(default=None)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100, default=None)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='cars')
    from_time = models.DateField(null=True, default=None)
    to_time = models.DateField(null=True, default=None)

    class Meta:
        db_table = 'order'
