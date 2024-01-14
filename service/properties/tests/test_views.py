import json
from datetime import datetime

from django.test import TestCase
from properties.models import County
from properties.models import Property
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory


class PropertiesListViewTests(TestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.property_dublin_1 = Property.objects.create(
            county=County.DUBLIN,
            digest="property_dublin_1_digest",
            postal_code="property_dublin_1_postal_code",
            price=100000,
            raw_address="property_dublin_1_raw_address",
            sale_date=datetime.now().date(),
        )
        self.property_dublin_2 = Property.objects.create(
            county=County.DUBLIN,
            digest="property_dublin_2_digest",
            postal_code="property_dublin_2_postal_code",
            price=200000,
            raw_address="property_dublin_2_raw_address",
            sale_date=datetime.now().date(),
        )
        self.property_mayo_1 = Property.objects.create(
            county=County.MAYO,
            digest="property_mayo_1_digest",
            postal_code="property_mayo_1_postal_code",
            price=300000,
            raw_address="property_mayo_1_raw_address",
            sale_date=datetime.now().date(),
        )

    def test_list_properties(self):
        response = self.client.get("/v1/properties")
        self.assertEqual(response.status_code, HTTP_200_OK)
        json_response = json.loads(response.content)
        self.assertEqual(json_response["count"], 3)
        self.assertEqual(json_response["results"][0]["id"], str(self.property_dublin_1.id))
        self.assertEqual(json_response["results"][1]["id"], str(self.property_dublin_2.id))
        self.assertEqual(json_response["results"][2]["id"], str(self.property_mayo_1.id))

    def test_list_properties_with_filter(self):
        response = self.client.get(f"/v1/properties?county={County.DUBLIN}")
        self.assertEqual(response.status_code, HTTP_200_OK)
        json_response = json.loads(response.content)
        self.assertEqual(json_response["count"], 2)
        self.assertEqual(json_response["results"][0]["id"], str(self.property_dublin_1.id))
        self.assertEqual(json_response["results"][1]["id"], str(self.property_dublin_2.id))

    def test_stats_properties(self):
        response = self.client.get("/v1/properties/stats?aggregation=count")
        self.assertEqual(response.status_code, HTTP_200_OK)
        json_response = json.loads(response.content)
        self.assertEqual(json_response["value"], 3)

    def test_stats_properties_with_filter(self):
        response = self.client.get(f"/v1/properties/stats?aggregation=count&county={County.MAYO}")
        self.assertEqual(response.status_code, HTTP_200_OK)
        json_response = json.loads(response.content)
        self.assertEqual(json_response["value"], 1)
