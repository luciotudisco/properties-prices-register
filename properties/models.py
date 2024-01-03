import uuid

from django.db import models


class Property(models.Model):
    place_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sale_date = models.DateField()
    eircode = models.CharField(max_length=7)
    formatted_address = models.CharField(max_length=500)
    county = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=10)
    latitude = models.DecimalField(max_digits=22, decimal_places=16)
    longitude = models.DecimalField(max_digits=22, decimal_places=16)
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
