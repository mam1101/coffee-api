from django.db import models
from django.conf import settings
import googlemaps
from django.template.defaultfilters import slugify
from api.models import BaseModel
from api.utils import generate_unique_slug
from django.db.models.fields.related import OneToOneField
from location_field.models.plain import PlainLocationField

gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)

class Address(BaseModel):
    address_1 = models.CharField(max_length=256)
    address_2 = models.CharField(max_length=256, blank=True)
    city = models.CharField(max_length=256)
    state = models.CharField(max_length=256)
    postal_code = models.CharField(max_length=5)
    country = models.CharField(max_length=3)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'


class OperatingHours(BaseModel):
    open_time = models.TimeField()
    close_time = models.TimeField()
    mon_open = models.BooleanField(default=False)
    tue_open = models.BooleanField(default=False)
    wed_open = models.BooleanField(default=False)
    thu_open = models.BooleanField(default=False)
    fri_open = models.BooleanField(default=False)
    sat_open = models.BooleanField(default=False)
    sun_open = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Operating Hours'
        verbose_name_plural = 'Operating Hours'


class LocationModel(BaseModel):
    full_address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True)
    latitude = models.DecimalField(decimal_places=8, max_digits=15)
    longitude = models.DecimalField(decimal_places=8, max_digits=15)
    operating_hours = OneToOneField(OperatingHours, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        geocode_result = gmaps.geocode(f'{self.full_address.address_1}, {self.full_address.city}, {self.full_address.state}')
        print(geocode_result)
        if geocode_result[0] is not None:
            self.latitude = geocode_result[0]['geometry']['location']['lat']
            self.longitude = geocode_result[0]['geometry']['location']['lng']
        super(LocationModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Cafe(LocationModel):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, default='', blank=True)

    def save(self, *args, **kwargs):
        if self.name is not None:
            self.slug = generate_unique_slug(self.name)
        super(Cafe, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Cafe'
        verbose_name_plural = 'Cafes'


class Distributer(LocationModel):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, default='', blank=True)

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        if self.name is not None:
            self.slug = generate_unique_slug(self.name)
        super(Distributer, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Distributer'
        verbose_name_plural = 'Distributers'


class Roastery(LocationModel):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, default='', blank=True)

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        if self.name is not None:
            self.slug = generate_unique_slug(self.name)
        super(Roastery, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Roastery'
        verbose_name_plural = 'Roasteries'