from rest_framework import serializers

from .models import ComputedBookPrice


class ComputedBookPriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = ComputedBookPrice
        fields = ('name', 'computed_price')
        read_only_fields = ('name', 'computed_price')

