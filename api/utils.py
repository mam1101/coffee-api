import random
import string

from django.template.defaultfilters import slugify

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def generate_unique_slug(text):
    return slugify(text) + random_string_generator(size=4)