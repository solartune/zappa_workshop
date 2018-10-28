from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('name', 'quantity', 'price')
        read_only_fields = ('name', 'quantity', 'price')

