from rest_framework import viewsets, mixins

from .models import ComputedBookPrice
from .serializers import ComputedBookPriceSerializer


class ComputedBookPriceViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = ComputedBookPrice.objects.all()
    serializer_class = ComputedBookPriceSerializer
