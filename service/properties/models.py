import uuid

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
