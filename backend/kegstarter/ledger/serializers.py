from rest_framework import serializers

from . import models


class LedgerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Ledger
        fields = ('url', 'pk', 'name', 'user')


class LedgerEntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.LedgerEntry
        fields = ('url', 'pk', 'amount', 'time', 'ledger', 'notes', 'user', 'guest_name')
