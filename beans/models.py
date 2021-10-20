from enum import unique
from django.db import models
from api.models import BaseModel
from django.template.defaultfilters import slugify

from api.utils import generate_unique_slug
from shops.models import Roastery


class TastingNote(BaseModel):
    name = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=256, default='', blank=True)

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        if self.name is not None:
            self.slug = generate_unique_slug(self.name)
        super(TastingNote, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Tasting Note'
        verbose_name_plural = 'Tasting Notes'


class Bean(BaseModel):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, default='', blank=True)
    tasting_notes = models.ManyToManyField(TastingNote, blank=True)
    roastery = models.ForeignKey(Roastery, on_delete=models.SET_NULL, null=True)
    roasted_on_date = models.DateField(null=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if self.name is not None:
            self.slug = generate_unique_slug(self.name)
        super(Bean, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Bean'
        verbose_name_plural = 'Beans'