from django.conf import settings

import requests
from zappa.async import task

from .models import ComputedBookPrice


@task
def get_data():
    url = f'http://{settings.COMPUTE_ENGINE_URL}/api/books/computed-prices'
    response = requests.get(url)
    data = response.json().get('data')
    for item in data:
        ComputedBookPrice.objects.update_or_create(
            name=item['name'], computed_price=item['computed_price'])


