from properties.models import Property
from rest_framework import serializers


class PropertySerializer(serializers.ModelSerializer):
    """
    Serializer class for the Property model.
    """

    property_type = serializers.ReadOnlyField()
    full_price = serializers.ReadOnlyField()

    class Meta:
        model = Property
        fields = "__all__"
