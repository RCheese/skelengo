from django_filters import rest_framework as filters

from .models import Ship


class ShipFilter(filters.FilterSet):
    class Meta:
        model = Ship
        fields = ("id", "title")
