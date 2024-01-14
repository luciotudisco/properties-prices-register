import uuid
from datetime import datetime
from unittest import mock

from django.test import TestCase
from properties.models import Property
from properties.signals import on_property_post_save


class UtilsTestCase(TestCase):
    @mock.patch("properties.signals.algolia_properties_index.save_object")
    def test_on_property_post_save(self, mock_save_object):
        property = Property(
            id=uuid.uuid4(),
            area="foo_bar_area",
            county="foo_bar_county",
            description="foo_bar_description",
            formatted_address="foo_bar_formatted_address",
            house="foo_bar_house",
            latitude="1.1",
            locality="foo_bar_locality",
            location_type="foo_bar_location_type",
            longitude="2.2",
            neighborhood="foo_bar_neighborhood",
            postal_code="foo_bar_postal_code",
            price="123456",
            raw_address="foo_bar_raw_address",
            region="foo_bar_raw_region",
            sale_date=datetime.now().date(),
            street="foo_bar_street",
        )
        on_property_post_save(sender=type(property), instance=property, created=True)

        mock_save_object.assert_called_once_with(
            {
                "objectID": property.id,
                "area": property.area,
                "county": property.county,
                "description": property.description,
                "formatted_address": property.formatted_address,
                "house": property.house,
                "latitude": property.latitude,
                "locality": property.locality,
                "location_type": property.location_type,
                "longitude": property.longitude,
                "neighborhood": property.neighborhood,
                "postal_code": property.postal_code,
                "price": property.price,
                "raw_address": property.raw_address,
                "region": property.region,
                "sale_date": property.sale_date.strftime("%x"),
                "street": property.street,
            }
        )
