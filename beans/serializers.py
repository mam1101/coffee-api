from rest_framework import serializers

from beans.models import Bean, TastingNote

class BeanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bean
        fields = ['id', 'name', 'slug', 'roastery', 'tasting_notes']
        depth = 2


class TastingNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TastingNote
        fields = ['id', 'name', 'slug']