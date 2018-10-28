import random

from zappa.async import task

from .models import Book

NAMES = [
    'Nice book', 'Even nicer book', 'Best team ever',
    'How to rule the world', 'How to make money', 'How to have fun'
]


@task
def generate_books():
    for name in NAMES:
        Book.objects.update_or_create(
            name=name, defaults={
                'quantity': random.randint(1, 1000),
                'price': random.randint(20, 150)}
        )


