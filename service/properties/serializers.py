from rest_framework import serializers

from .models import Property


class PropertySerializer(serializers.ModelSerializer):
    """
    Serializer class for the Property model.
    """

    class Meta:
        model = Property
        fields = "__all__"
