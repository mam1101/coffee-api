from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework import filters
from beans.models import Bean, TastingNote
from rest_framework.routers import SimpleRouter

from beans.serializers import BeanSerializer, TastingNoteSerializer


class BeanViewSet(ModelViewSet):
    serializer_class = BeanSerializer
    queryset = Bean.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name', 'roastery__name']


class TastingNoteViewSet(ModelViewSet):
    serializer_class = TastingNoteSerializer
    queryset = TastingNote.objects.all()


router = SimpleRouter()
router.register(r'beans', BeanViewSet, basename='Beans')
router.register(r'tasting-notes', TastingNoteViewSet, basename='Tasting Notes')