import uuid
from decimal import Decimal

from django.db import models


class County(models.TextChoices):
    """
    Counties in Ireland.
    """

    CARLOW = "Carlow"
    CAVAN = "Cavan"
    CLARE = "Clare"
    CORK = "Cork"
    DONEGAL = "Donegal"
    DUBLIN = "Dublin"
    GALWAY = "Galway"
    KERRY = "Kerry"
    KILDARE = "Kildare"
    KILKENNY = "Kilkenny"
    LAOIS = "Laois"
    LEITRIM = "Leitrim"
    LIMERICK = "Limerick"
    LONGFORD = "Longford"
    LOUTH = "Louth"
    MAYO = "Mayo"
    MEATH = "Meath"
    MONAGHAN = "Monaghan"
    OFFALY = "Offaly"
    ROSCOMMON = "Roscommon"
    SLIGO = "Sligo"
    TIPPERARY = "Tipperary"
    WATERFORD = "Waterford"
    WESTMEATH = "Westmeath"
    WEXFORD = "Wexford"
    WICKLOW = "Wicklow"


class PropertyType(models.TextChoices):
    """
    Types of properties.
    """

    NEW_BUILD = "New Build"
    SECOND_HAND = "Second Hand"
    OTHER = "Other"


class Property(models.Model):
    """
    Represents a sold property with various attributes.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    area = models.CharField(max_length=100, null=True, blank=True)
    county = models.CharField(choices=County.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    digest = models.CharField(max_length=32, unique=True)
    formatted_address = models.CharField(max_length=500, null=True, blank=True)
    house = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.DecimalField(max_digits=22, decimal_places=6, null=True, blank=True)
    locality = models.CharField(max_length=100, null=True, blank=True)
    location_type = models.CharField(max_length=100, null=True, blank=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=6, null=True, blank=True)
    neighborhood = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    raw_address = models.CharField(max_length=500, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    sale_date = models.DateField()
    street = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def property_type(self):
        """
        Determines the type of the property based on its description.

        Returns:
            PropertyType: The type of the property.
        """
        description_lower = self.description.lower() if self.description else None
        if description_lower in ["new dwelling house /apartment", "teach/árasán cónaithe nua"]:
            return PropertyType.NEW_BUILD
        elif description_lower in ["second-hand dwelling house /apartment", "teach/árasán cónaithe atháimhe"]:
            return PropertyType.SECOND_HAND
        else:
            return PropertyType.OTHER

    @property
    def full_price(self):
        """
        Calculates the full price of the property.

        If the property type is NEW_BUILD, the price is multiplied by 1.135 to include 13.5% VAT.
        Otherwise, the original price is returned.

        Returns:
            str: the full price of the property.
        """
        if self.property_type == PropertyType.NEW_BUILD:
            price_with_vat = (Decimal(self.price) * Decimal("1.135")).quantize(Decimal("1"))
            price_thousands_reminder = price_with_vat % 1000
            price_rounding_amount = 1000 - price_thousands_reminder if price_thousands_reminder != 0 else 0
            if price_thousands_reminder <= 5:
                return str(price_with_vat - price_rounding_amount)
            elif price_thousands_reminder >= 995:
                return str(price_with_vat + price_rounding_amount)
            return str(price_with_vat)
        return self.price
