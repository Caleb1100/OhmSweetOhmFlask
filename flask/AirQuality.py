import random

def get_air_quality():
    return 'Good' if random.random() > 0.5 else 'Poor'
