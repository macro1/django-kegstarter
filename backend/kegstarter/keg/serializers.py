from rest_framework import serializers

from . import models


class TapSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tap
        fields = ('pk', 'location')


class KegSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Keg
        fields = ('pk', 'beer', 'gallons', 'purchase_date', 'tap')
