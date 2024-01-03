from rest_framework import generics

from .models import Property
from .serializers import PropertySerializer


class PropertiesListView(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    http_method_names = ["get"]
