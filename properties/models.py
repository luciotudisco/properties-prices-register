import uuid

from django.db import models


class County(models.TextChoices):
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
    place_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sale_date = models.DateField()
    eircode = models.CharField(max_length=7)
    formatted_address = models.CharField(max_length=500)
    county = models.CharField(choices=County.choices)
    price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    latitude = models.DecimalField(
        max_digits=22, decimal_places=16, null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=22, decimal_places=16, null=True, blank=True
    )
    description = models.CharField(max_length=500)
    is_full_market_price = models.BooleanField(default=True)
    administrative_area_level_1 = models.CharField(max_length=100)
    administrative_area_level_2 = models.CharField(max_length=100)
    administrative_area_level_3 = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    route = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100)
    street_number = models.CharField(max_length=100)
    sublocality = models.CharField(max_length=100)
    stree_view_image_url = models.URLField(max_length=200)
