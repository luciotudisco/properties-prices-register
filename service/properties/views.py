from django_filters.rest_framework import DjangoFilterBackend
from drf_aggregation.filters import TruncateDateFilter
from drf_aggregation.viewsets import AggregationViewSet
from properties.models import Property
from properties.serializers import PropertySerializer
from rest_framework import generics


class PropertiesListView(generics.ListAPIView):
    filterset_fields = {
        "county": ["exact", "in"],
        "locality": ["exact", "in"],
        "neighborhood": ["exact", "in"],
        "street": ["exact", "in"],
        "price": ["gte", "lte"],
        "sale_date": ["gte", "lte"],
    }
    filter_backends = [DjangoFilterBackend]
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class PropertiesStatsView(AggregationViewSet):
    filterset_fields = {
        "county": ["exact", "in"],
        "locality": ["exact", "in"],
        "neighborhood": ["exact", "in"],
        "street": ["exact", "in"],
        "price": ["gte", "lte"],
        "sale_date": ["gte", "lte"],
    }
    filter_backends = [TruncateDateFilter, DjangoFilterBackend]
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
