from collections import namedtuple
import random
import string
import time


def get_populations():
    pop = namedtuple('city', ['city', 'population', 'continent'])
    populations = [
        ('Berlin', 3.7, 'eu'),
        ('Auckland', 1.7, 'pac'),
        ('London', 8.9, 'eu'),
        ('Sheffield', 0.5, 'eu'),
        ('Christchurch', 0.38, 'pac')
    ]
    return [pop(*p) for p in populations]


def compute_intensive_task(word_length):
    return ''.join([random.choice(string.ascii_letters) for _ in range(word_length)])