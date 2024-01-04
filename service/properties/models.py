import uuid

from django.db import models


class County(models.TextChoices):
    """
    Represents the counties in Ireland.
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

    place_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sale_date = models.DateField()
    raw_address = models.CharField(max_length=500, null=True, blank=True)
    formatted_address = models.CharField(max_length=500, null=True, blank=True)
    county = models.CharField(choices=County.choices)
    price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    lat = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
    lng = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    locality = models.CharField(max_length=100, null=True, blank=True)
    sublocality = models.CharField(max_length=100, null=True, blank=True)
    premise = models.CharField(max_length=100, null=True, blank=True)
    subpremise = models.CharField(max_length=100, null=True, blank=True)
    neighborhood = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=100, null=True, blank=True)
    postal_town = models.CharField(max_length=100, null=True, blank=True)
    route = models.CharField(max_length=100, null=True, blank=True)
    stree_view_image_url = models.URLField(max_length=500, null=True, blank=True)
    digest = models.CharField(max_length=32, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
