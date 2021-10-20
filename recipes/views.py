from rest_framework import filters
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from recipes.models import Ingredient, IngredientMeasurement, Recipe
from rest_framework.routers import SimpleRouter

from recipes.serializers import IngredientMeasurementSerializer, IngredientSerializer, RecipeSerializer


class IngredientViewSet(ModelViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()


class IngredientMeasurementViewSet(ModelViewSet):
    serializer_class = IngredientMeasurementSerializer
    queryset = IngredientMeasurement.objects.all()


class RecipeViewSet(ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name']


router = SimpleRouter()
router.register(r'ingredients', IngredientViewSet, basename='Ingredients')
router.register(r'ingredient-measurements', IngredientMeasurementViewSet, basename='Ingredient Measurements')
router.register(r'recipes', RecipeViewSet, basename='Recipes')