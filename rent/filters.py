import django_filters
from rent.models import HouseDetail


class HouseDetailFilter(django_filters.FilterSet):
    class Meta:
        model = HouseDetail
        fields = ['location', 'rent_type']
