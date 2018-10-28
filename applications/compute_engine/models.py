from django.db import models


class ComputedBookPrice(models.Model):

    name = models.CharField(max_length=128)
    computed_price = models.DecimalField(max_digits=6, decimal_places=2)
