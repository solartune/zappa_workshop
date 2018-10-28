from django.conf import settings

import requests
from zappa.async import task

from .models import ComputedBookPrice


@task
def get_data():
    url = f'http://{settings.BOOKS_URL}/api/books'
    response = requests.get(url)
    data = response.json().get('data')
    for item in data:
        computed_price = item['quantity'] * item['price']

        ComputedBookPrice.objects.update_or_create(
            name=item['name'], defaults={'computed_price': computed_price})


