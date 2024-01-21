from properties.models import Property
from rest_framework import serializers


class PropertySerializer(serializers.ModelSerializer):
    """
    Serializer class for the Property model.
    """

    class Meta:
        model = Property
        fields = "__all__"
