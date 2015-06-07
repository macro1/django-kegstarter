from django.contrib import auth

from rest_framework import permissions, routers, viewsets

from . import serializers

API_ROUTER = routers.DefaultRouter()


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = auth.get_user_model().objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]
API_ROUTER.register(r'user', UserViewSet)
