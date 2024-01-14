import decimal
import random
import string
import textwrap
from datetime import datetime
from unittest import mock

from django.test import TestCase
from ppr.settings import PROPERTY_PRICE_REGISTER_BASE_URL
from properties.models import County
from properties.models import Property
from properties.tasks import load_properties
from properties.tasks import load_properties_for_county_and_date
from properties.tasks import load_property
from requests import HTTPError


class TasksTestCase(TestCase):
    @mock.patch("properties.tasks.datetime")
    @mock.patch("properties.tasks.load_properties_for_county_and_date.delay")
    def test_load_properties_with_default_lookback_months(self, mock_delay, mock_datetime):
        mock_datetime.today.return_value = datetime(2023, 12, 1)

        load_properties()

        expected_calls = [mock.call(county=county, month="12", year="2023") for county in County.values]
        mock_delay.assert_has_calls(expected_calls)

    @mock.patch("properties.tasks.datetime")
    @mock.patch("properties.tasks.load_properties_for_county_and_date.delay")
    def test_load_properties_with_custom_lookback_months(self, mock_delay, mock_datetime):
        mock_datetime.today.return_value = datetime(2023, 12, 1)

        load_properties(3)

        expected_calls = [mock.call(county=county, month="12", year="2023") for county in County.values]
        expected_calls.extend([mock.call(county=county, month="11", year="2023") for county in County.values])
        expected_calls.extend([mock.call(county=county, month="10", year="2023") for county in County.values])
        mock_delay.assert_has_calls(expected_calls)

    @mock.patch("requests.get")
    @mock.patch("properties.tasks.load_property.delay")
    def test_load_properties_for_county_and_date(self, mock_load_property, mock_get):
        mock_text = """
        Date of Sale (dd/mm/yyyy),Address,County,Eircode,Price (€),Not Full Market Price,VAT Exclusive,Description of Property
        "01/12/2023","1 CILL CLUAIN, LOUISBURGH","Mayo","F28KR63","€320,000.00","No","No","Second-Hand Dwelling house /Apartment"
        "01/12/2023","14 SHANAGHY HEIGHTS, BALLINA","Mayo","F26A4V6","€201,000.00","No","No","Second-Hand Dwelling house /Apartment"
        """
        mock_get.return_value.text = textwrap.dedent(mock_text)

        load_properties_for_county_and_date(county=County.MAYO, month="12", year="2023")

        expected_calls = [
            mock.call(
                sale_date=datetime(2023, 12, 1).date(),
                address="1 CILL CLUAIN, LOUISBURGH",
                county=County.MAYO,
                price="320000.00",
                postal_code="F28KR63",
                description="Second-Hand Dwelling house /Apartment",
            ),
            mock.call(
                sale_date=datetime(2023, 12, 1).date(),
                address="14 SHANAGHY HEIGHTS, BALLINA",
                county=County.MAYO,
                price="201000.00",
                postal_code="F26A4V6",
                description="Second-Hand Dwelling house /Apartment",
            ),
        ]
        mock_load_property.assert_has_calls(expected_calls)

        csv_file_name = "PPR-2023-12-Mayo.csv"
        mock_get.assert_called_with(url=f"{PROPERTY_PRICE_REGISTER_BASE_URL}/Downloads/{csv_file_name}/$FILE/{csv_file_name}", timeout=30)

    @mock.patch("requests.get")
    @mock.patch("properties.tasks.load_property.delay")
    def test_load_properties_for_county_and_date_with_error(self, mock_load_property, mock_get):
        mock_response = mock.Mock()
        mock_response.raise_for_status = mock.Mock()
        mock_response.raise_for_status.side_effect = HTTPError("Oops, something went wrong!")
        mock_get.return_value = mock_response

        load_properties_for_county_and_date(county=County.MAYO, month="12", year="2023")

        mock_load_property.assert_not_called()

        csv_file_name = "PPR-2023-12-Mayo.csv"
        mock_get.assert_called_with(url=f"{PROPERTY_PRICE_REGISTER_BASE_URL}/Downloads/{csv_file_name}/$FILE/{csv_file_name}", timeout=30)

    @mock.patch("properties.tasks.geocode_address")
    def test_load_property_with_empty_geocode(self, mock_geocode):
        mock_geocode.return_value = None

        sale_date = datetime(2023, 12, 1).date()
        address = "".join(random.choices(string.ascii_uppercase + string.digits, k=100))  # nosec
        county = County.MAYO
        postal_code = "".join(random.choices(string.ascii_uppercase + string.digits, k=20))  # nosec
        price = random.randint(100000, 1000000)  # nosec
        description = "Second-Hand Dwelling house /Apartment"

        load_property(
            sale_date=sale_date,
            address=address,
            county=county,
            price=price,
            postal_code=postal_code,
            description=description,
        )

        property = Property.objects.get(raw_address=address)
        self.assertEqual(sale_date, property.sale_date)
        self.assertEqual(county, property.county)
        self.assertEqual(price, property.price)
        self.assertEqual(postal_code, property.postal_code)
        self.assertEqual(description, property.description)
        self.assertIsNotNone(property.digest)

    @mock.patch("properties.tasks.geocode_address")
    def test_load_property_with_geocode(self, mock_geocode):
        geo_code_result = {
            "address": "14 Shanaghy Heights, Ardnaree Or Shanaghy, Ballina, Co. Mayo, F26 A4V6, Ireland",
            "postal_code": "F26 A4V6",
            "region": "County Mayo",
            "locality": "Ballina",
            "neighborhood": "Ardnaree Or Shanaghy",
            "street": "Shanaghy Heights",
            "house": "14",
            "location": {"lat": 54.107894, "lng": -9.141489},
            "location_type": "exact",
        }
        mock_geocode.return_value = geo_code_result

        sale_date = datetime(2023, 12, 1).date()
        address = "".join(random.choices(string.ascii_uppercase + string.digits, k=100))  # nosec
        county = County.MAYO
        postal_code = "".join(random.choices(string.ascii_uppercase + string.digits, k=20))  # nosec
        price = random.randint(100000, 1000000)  # nosec
        description = "Second-Hand Dwelling house /Apartment"

        load_property(
            sale_date=sale_date,
            address=address,
            county=county,
            price=price,
            postal_code=postal_code,
            description=description,
        )

        property = Property.objects.get(raw_address=address)
        self.assertEqual(sale_date, property.sale_date)
        self.assertEqual(county, property.county)
        self.assertEqual(price, property.price)
        self.assertEqual(postal_code, property.postal_code)
        self.assertEqual(description, property.description)
        self.assertEqual(geo_code_result["address"], property.formatted_address)
        self.assertEqual(geo_code_result["house"], property.house)
        self.assertEqual(geo_code_result["locality"], property.locality)
        self.assertEqual(geo_code_result["location_type"], property.location_type)
        self.assertEqual(decimal.Decimal(geo_code_result["location"]["lat"]).quantize(decimal.Decimal(".000001")), property.latitude)
        self.assertEqual(decimal.Decimal(geo_code_result["location"]["lng"]).quantize(decimal.Decimal(".000001")), property.longitude)
        self.assertEqual(geo_code_result["neighborhood"], property.neighborhood)
        self.assertEqual(geo_code_result["region"], property.region)
        self.assertEqual(geo_code_result["street"], property.street)
        self.assertIsNotNone(property.digest)

    @mock.patch("properties.tasks.geocode_address")
    def test_load_property_with_same_digest(self, mock_geocode):
        mock_geocode.return_value = None
        sale_date = datetime(2023, 12, 1).date()
        address = "".join(random.choices(string.ascii_uppercase + string.digits, k=100))  # nosec
        county = County.MAYO
        postal_code = "".join(random.choices(string.ascii_uppercase + string.digits, k=20))  # nosec
        price = random.randint(100000, 1000000)  # nosec
        description = "Second-Hand Dwelling house /Apartment"

        load_property(
            sale_date=sale_date,
            address=address,
            county=county,
            price=price,
            postal_code=postal_code,
            description=description,
        )

        load_property(
            sale_date=sale_date,
            address=address,
            county=county,
            price=price,
            postal_code=postal_code,
            description=description,
        )

        properties_count = Property.objects.filter(raw_address=address).count()
        self.assertEqual(1, properties_count)
