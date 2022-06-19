from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='brands/')

    class Meta:
        db_table = 'brand'
        ordering = ['id']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='categories/')

    class Meta:
        db_table = 'category'
        ordering = ['id']

    def __str__(self):
        return self.name


class Car(models.Model):
    TRANSMISSION = (
        (1, 'Auto'),
        (2, 'Manual')
    )

    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='cars/')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, related_name='brand')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='category')
    doors = models.IntegerField(default=4)
    seats = models.IntegerField(default=4)
    buggage = models.IntegerField()
    transmission = models.IntegerField(choices=TRANSMISSION, default=1)
    conditioner = models.BooleanField(default=False)
    fuel = models.CharField(max_length=255)
    insurance = models.FloatField()
    price = models.FloatField()

    class Meta:
        db_table = 'car'
        ordering = ['id']

    def __str__(self):
        return self.name
