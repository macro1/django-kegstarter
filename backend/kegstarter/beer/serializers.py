from rest_framework import serializers

from . import models


class BeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Beer
        fields = ('pk', 'name', 'brewer', 'abv')


class BrewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brewer
        fields = ('pk', 'name', 'beer_set')
