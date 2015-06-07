from rest_framework import viewsets, routers

from kegstarter.utils.permissions import IsStaffOrReadOnly
from . import models, serializers

API_ROUTER = routers.SimpleRouter()


class KegViewSet(viewsets.ModelViewSet):
    queryset = models.Keg.objects.all()
    serializer_class = serializers.KegSerializer
    permission_classes = [IsStaffOrReadOnly]
API_ROUTER.register(r'keg', KegViewSet)
