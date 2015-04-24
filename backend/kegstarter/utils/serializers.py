from django.contrib import auth

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = auth.get_user_model()
        fields = ('url', 'pk', 'username', 'first_name', 'last_name', 'date_joined')
