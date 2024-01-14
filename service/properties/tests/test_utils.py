from unittest import mock

from django.test import TestCase
from ppr.settings import GEOCODE_API_HOST
from ppr.settings import GEOCODE_API_KEY
from ppr.settings import GEOCODE_API_URL
from properties.utils import geocode_address
from requests import HTTPError


class UtilsTestCase(TestCase):
    @mock.patch("requests.get")
    def test_geocode_address(self, mock_get):
        expected_geo_code = {"foo": "bar"}
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"results": [expected_geo_code]}

        address = "foo bar address"
        actual_geo_code = geocode_address(address=address)
        self.assertEqual(expected_geo_code, actual_geo_code)

        mock_get.assert_called_with(
            url=GEOCODE_API_URL,
            headers={
                "X-RapidAPI-Key": GEOCODE_API_KEY,
                "X-RapidAPI-Host": GEOCODE_API_HOST,
            },
            params={
                "address": address,
                "language": "en",
                "country": "IE",
            },
            timeout=5,
        )

    @mock.patch("requests.get")
    def test_geocode_address_with_empty_results(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"results": []}

        address = "foo bar address"
        actual_geo_code = geocode_address(address=address)
        self.assertIsNone(actual_geo_code)

        mock_get.assert_called_with(
            url=GEOCODE_API_URL,
            headers={
                "X-RapidAPI-Key": GEOCODE_API_KEY,
                "X-RapidAPI-Host": GEOCODE_API_HOST,
            },
            params={
                "address": address,
                "language": "en",
                "country": "IE",
            },
            timeout=5,
        )

    @mock.patch("requests.get")
    def test_geocode_address_with_error(self, mock_get):
        mock_response = mock.Mock()
        mock_response.raise_for_status = mock.Mock()
        mock_response.raise_for_status.side_effect = HTTPError("Oops, something went wrong!")
        mock_get.return_value = mock_response

        actual_geo_code = geocode_address("foo bar address ")
        self.assertIsNone(actual_geo_code)
