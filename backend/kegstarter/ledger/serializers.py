from rest_framework import serializers

from . import models


class LedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ledger
        fields = ('pk', 'name', 'user')


class LedgerEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LedgerEntry
        fields = ('pk', 'amount', 'time', 'ledger', 'notes', 'user', 'guest_name')
