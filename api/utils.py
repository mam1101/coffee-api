import random
import string
from django.conf import settings
import googlemaps
from django.template.defaultfilters import slugify

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def generate_unique_slug(text):
    return slugify(text) + random_string_generator(size=4)

def search_place(query, lat, lng, radius=25):
    gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
    return gmaps.places(query, location=f"{lat}, {lng}", radius=radius)