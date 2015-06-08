from rest_framework import viewsets

from kegstarter.api import routers
from kegstarter.utils.permissions import IsStaffOrReadOnly
from . import models, serializers

API_ROUTER = routers.api_router.app_router('beer')


class BeerViewSet(viewsets.ModelViewSet):
    queryset = models.Beer.objects.all()
    serializer_class = serializers.BeerSerializer
    permission_classes = [IsStaffOrReadOnly]
API_ROUTER.register(r'beer', BeerViewSet)


class BrewerViewSet(viewsets.ModelViewSet):
    queryset = models.Brewer.objects.all()
    serializer_class = serializers.BrewerSerializer
    permission_classes = [IsStaffOrReadOnly]
API_ROUTER.register(r'brewer', BrewerViewSet)
