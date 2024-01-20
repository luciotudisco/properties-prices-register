from properties.models import Property
from rest_framework import serializers


class PropertySerializer(serializers.ModelSerializer):
    """
    Serializer class for the Property model.
    """

    property_type = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = "__all__"

    def get_property_type(self, instance) -> str:
        description_lower = instance.description.lower() if instance.description else None
        if description_lower in ["new dwelling house /apartment", "teach/árasán cónaithe nua"]:
            return "NEW_BUILD"
        elif description_lower in ["second-hand dwelling house /apartment", "teach/árasán cónaithe atháimhe"]:
            return "SECOND_HAND"
        else:
            return "OTHER"
