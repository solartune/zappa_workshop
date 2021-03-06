from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ComputedBookPriceViewSet


router = DefaultRouter()

router.register(
    r'computed-prices',
    ComputedBookPriceViewSet,
    base_name='computed_book_price'
)


urlpatterns = [
    path('api/', include(router.urls)),
]
