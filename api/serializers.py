from rest_framework import serializers
from api.models import House


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House