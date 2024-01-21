import uuid
from datetime import datetime

from django.test import TestCase
from properties.models import Property
from properties.models import PropertyType


class ModelsTestCase(TestCase):
    def test_property_type_other(self):
        property = Property(
            id=uuid.uuid4(),
            county="foo_bar_county",
            description="foo_bar_description",
            price="123456",
            raw_address="foo_bar_raw_address",
            sale_date=datetime.now().date(),
        )
        self.assertEqual(property.property_type, PropertyType.OTHER)

    def test_property_type_second_hand(self):
        property = Property(
            id=uuid.uuid4(),
            county="foo_bar_county",
            description="Second-Hand Dwelling house /Apartment",
            price="123456",
            raw_address="foo_bar_raw_address",
            sale_date=datetime.now().date(),
        )
        self.assertEqual(property.property_type, PropertyType.SECOND_HAND)

    def test_property_type_new_build(self):
        property = Property(
            id=uuid.uuid4(),
            county="foo_bar_county",
            description="New Dwelling house /Apartment",
            price="123456",
            raw_address="foo_bar_raw_address",
            sale_date=datetime.now().date(),
        )
        self.assertEqual(property.property_type, PropertyType.NEW_BUILD)

    def test_property_vat_inclusive_price_second_hand(self):
        property = Property(
            id=uuid.uuid4(),
            county="foo_bar_county",
            description="Second-Hand Dwelling house /Apartment",
            price="458149.78",
            raw_address="foo_bar_raw_address",
            sale_date=datetime.now().date(),
        )
        self.assertEqual(
            property.full_price,
            "458149.78",
        )

    def test_property_vat_inclusive_price_new_build(self):
        property = Property(
            id=uuid.uuid4(),
            county="foo_bar_county",
            description="New Dwelling house /Apartment",
            price="458149.78",
            raw_address="foo_bar_raw_address",
            sale_date=datetime.now().date(),
        )
        self.assertEqual(
            property.full_price,
            "520000.00",
        )
