from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .models import Property
from .serializers import PropertySerializer


class PropertiesListView(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["county"]
    http_method_names = ["get"]
