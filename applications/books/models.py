from django.db import models


class Book(models.Model):

    name = models.CharField(max_value=128)
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

