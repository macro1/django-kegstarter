from rest_framework import viewsets

from kegstarter.api import routers
from kegstarter.utils.permissions import IsStaffOrReadOnly
from . import models, serializers


API_ROUTER = routers.api_router.app_router('keg')


class KegViewSet(viewsets.ModelViewSet):
    queryset = models.Keg.objects.all()
    serializer_class = serializers.KegSerializer
    permission_classes = [IsStaffOrReadOnly]
API_ROUTER.register(r'keg', KegViewSet)
