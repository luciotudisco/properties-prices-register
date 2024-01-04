import csv
import re
from datetime import date, datetime, timedelta
from typing import Any, Dict, List, Optional

import requests
from celery import shared_task

from .functions import get_geocode
from .models import County, Property

BASE_URL = "https://www.propertypriceregister.ie/website/npsra/ppr/npsra-ppr.nsf"


@shared_task(name="load_properties")
def load_properties():
    load_date = datetime.now() - timedelta(days=10)
    for county in County.values:
        csv_file_name = f"PPR-{load_date.year}-{load_date.month}-{county}.csv"
        url = f"{BASE_URL}/Downloads/{csv_file_name}/$FILE/{csv_file_name}"
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        reader = csv.DictReader(response.text.splitlines())
        for row in reader:
            property_data = list(row.values())
            _create_property(
                sale_date=datetime.strptime(property_data[0], "%d/%m/%Y").date(),
                address=property_data[1],
                county=county,
                price=re.sub(r"[^\d.]", "", property_data[4]),
                eircode=property_data[2],
                description=property_data[7],
            )


def _create_property(
    sale_date: date,
    address: str,
    county: str,
    price: str,
    eircode: Optional[str],
    description: Optional[str],
):
    geocode_result = get_geocode(address=address, county=county)
    # place_id = geocode_result[0]["place_id"]
    # place = get_place(place_id=place_id)
    Property.objects.update_or_create(
        sale_date=sale_date,
        formatted_address=address,
        county=county,
        defaults={
            "administrative_area_level_1": _get_address_component(
                geocode_result, "administrative_area_level_1"
            ),
            "administrative_area_level_2": _get_address_component(
                geocode_result, "administrative_area_level_2"
            ),
            "administrative_area_level_3": _get_address_component(
                geocode_result, "administrative_area_level_3"
            ),
            "locality": _get_address_component(geocode_result, "locality"),
            "neighborhood": _get_address_component(geocode_result, "neighborhood"),
            "postal_code": _get_address_component(geocode_result, "postal_code"),
            "route": _get_address_component(geocode_result, "route"),
            "street_address": _get_address_component(geocode_result, "street_address"),
            "street_number": _get_address_component(geocode_result, "street_number"),
            "sublocality": _get_address_component(geocode_result, "sublocality"),
            "eircode": eircode,
            "price": price,
            "description": description,
        },
    )


def _get_address_component(
    geocode_result: List[Dict[str, Any]], type: str
) -> Optional[str]:
    for address_component in geocode_result[0]["address_components"]:
        if type in address_component["types"]:
            return address_component["long_name"]
    return None
