from rest_framework import serializers

from recipes.models import Ingredient, IngredientMeasurement, Recipe

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']


class IngredientMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientMeasurement
        fields = ['id', 'unit', 'amount', 'ingredient']
        depth = 1


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'slug', 'ingredients']
        depth = 2
