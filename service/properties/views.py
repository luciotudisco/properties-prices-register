from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .models import Property
from .serializers import PropertySerializer


class PropertiesListView(generics.ListAPIView):
    queryset = Property.objects.all()
    http_method_names = ["get"]
    serializer_class = PropertySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        "sale_date": ["gte", "lte"],
        "county": ["exact"],
        "locality": ["exact"],
        "sublocality": ["exact"],
        "neighborhood": ["exact"],
        "price": ["gte", "lte"],
    }
