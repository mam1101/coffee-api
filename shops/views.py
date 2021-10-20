from rest_framework.viewsets import ModelViewSet
from rest_framework.routers import SimpleRouter
from rest_framework import filters

from shops.models import Cafe, Distributer, Roastery
from shops.serializers import CafeSerializer, DistributerSerializer, RoasterySerializer


class CafeViewSet(ModelViewSet):
    serializer_class = CafeSerializer
    queryset = Cafe.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name']


class DistributerViewSet(ModelViewSet):
    serializer_class = DistributerSerializer
    queryset = Distributer.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name']


class RoasteryViewSet(ModelViewSet):
    serializer_class = RoasterySerializer
    queryset = Roastery.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name']


router = SimpleRouter()
router.register(r'cafes', CafeViewSet, basename='Cafes')
router.register(r'distributers', DistributerViewSet, basename='Distributers')
router.register(r'roasteries', RoasteryViewSet, basename='Roasteries')