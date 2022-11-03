from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from .filters import ShipFilter
from .models import Ship
from .serializers import ShipSerializer


class ShipView(ReadOnlyModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)
    permission_classes = (IsAuthenticated,)
    queryset = Ship.objects.all()
    serializer_class = ShipSerializer
    filterset_class = ShipFilter
