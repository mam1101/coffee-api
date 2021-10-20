from django.contrib import admin

from recipes.models import Ingredient, IngredientMeasurement, Recipe


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(IngredientMeasurement)
class IngredientMeasurementAdmin(admin.ModelAdmin):
    pass


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass
