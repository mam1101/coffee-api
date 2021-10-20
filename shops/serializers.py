from rest_framework import serializers

from shops.models import Cafe, Distributer, Roastery

class CafeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cafe
        fields = ['id', 'name', 'slug', 'full_address', 'location', 'operating_hours']
        depth = 1


class DistributerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distributer
        fields = ['id', 'name', 'slug', 'full_address', 'location', 'operating_hours']
        depth = 1


class RoasterySerializer(serializers.ModelSerializer):
    class Meta:
        model = Roastery
        fields = ['id', 'name', 'slug', 'full_address', 'location', 'operating_hours', 'beans']
        depth = 1