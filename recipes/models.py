from django.db import models
from django.template.defaultfilters import slugify
from api.models import BaseModel
from api.utils import generate_unique_slug, random_string_generator



class Ingredient(BaseModel):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'


class IngredientMeasurement(BaseModel):
    unit = models.CharField(max_length=16)
    amount = models.DecimalField(default=0, decimal_places=2, max_digits=5)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.ingredient.name
    
    class Meta:
        verbose_name = 'Ingredient Measurement'
        verbose_name_plural = 'Ingredient Measurements'
    

class Recipe(BaseModel):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, default='', blank=True)
    ingredients = models.ManyToManyField(
        'IngredientMeasurement', blank=True
    )

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        if self.name is not None:
            self.slug = generate_unique_slug(self.name)
        super(Recipe, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'    
