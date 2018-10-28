from django.contrib import admin

from .models import ComputedBookPrice


@admin.register(ComputedBookPrice)
class ComputedBookPrice(admin.ModelAdmin):

    list_display = ('name', 'computed_price')