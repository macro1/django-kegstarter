from rest_framework import serializers

from . import models


class TapSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tap
        fields = ('pk', 'location')


class BeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Beer
        fields = ('pk', 'name', 'brewer', 'abv')


class BrewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brewer
        fields = ('pk', 'name', 'beer_set')


class KegSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Keg
        fields = ('pk', 'beer', 'gallons', 'purchase_date', 'tap')
