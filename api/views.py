#from django.shortcuts import render
from rest_framework import viewsets
from . import serializers, models


class HouseViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.HouseSerializer
    queryset = models.House.objects.all()
