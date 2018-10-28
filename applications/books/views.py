from rest_framework import viewsets, mixins

from .models import Book
from .serializers import BookSerializer


class BookViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
