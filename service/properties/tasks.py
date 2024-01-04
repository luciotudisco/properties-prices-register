import csv
import hashlib
import logging
import re
from datetime import date
from datetime import datetime
from datetime import timedelta
from typing import Any
from typing import Dict
from typing import Optional

import requests
from celery import shared_task

from .models import County
from .models import Property
from .utils import get_geocode_by_address
from .utils import index_object
from .utils import retrieve_and_store_streetview_image

logger = logging.getLogger("ppr.properties.tasks")
BASE_URL = "https://www.propertypriceregister.ie/website/npsra/ppr/npsra-ppr.nsf"
LOOKBACK_MONTHS_NUMBER = 1


@shared_task(name="load_properties")
def load_properties():
    """
    Initiate loading of properties for each Irish county and date within a specified lookback period.
    """
    logger.info("Loading properties ...")
    for month in range(LOOKBACK_MONTHS_NUMBER):
        sale_date = (datetime.now() - timedelta(days=30 * month)).date()
        for county in County.values:
            month = f"{sale_date:%m}"
            year = sale_date.year
            load_properties_for_county_and_date.delay(county, month, year)


@shared_task(name="load_properties_for_county_and_date")
def load_properties_for_county_and_date(county: str, month: str, year: str):
    logger.info("Retrieving properties for county [%s] and date [%s:%s] ...", county, year, month)
    try:
        csv_file_name = f"PPR-{year}-{month}-{county}.csv"
        url = f"{BASE_URL}/Downloads/{csv_file_name}/$FILE/{csv_file_name}"
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        reader = csv.DictReader(response.text.splitlines())
        for row in reader:
            property_data = list(row.values())
            load_property.delay(
                sale_date=datetime.strptime(property_data[0], "%d/%m/%Y").date(),
                address=property_data[1],
                county=county,
                price=re.sub(r"[^\d.]", "", property_data[4]),
                postal_code=property_data[3],
                description=property_data[7],
            )
    except Exception as e:
        logger.error("Error retrieving properties for county [%s] and date [%s:%s]: %s", county, year, month, e)


@shared_task(name="load_property")
def load_property(
    sale_date: date,
    address: str,
    county: str,
    price: str,
    postal_code: Optional[str],
    description: Optional[str],
):
    logger.info("Retrieving properties for county [%s] and address [%s] ...", county, address)
    geocode_result = get_geocode_by_address(address=address, county=county, postal_code=postal_code)
    if not geocode_result:
        logger.error("No geocode result found for address [%s]", address)
        return

    property_digest = hashlib.md5(f"{sale_date.isoformat()}#{address}#{price}".encode(), usedforsecurity=False).hexdigest()
    if Property.objects.filter(digest=property_digest).exists():
        logger.warning("Property with digest [%s] already exists", property_digest)
        return

    place_id = geocode_result["place_id"]
    lat = str(geocode_result["geometry"]["location"]["lat"])
    lng = str(geocode_result["geometry"]["location"]["lng"])
    stree_view_image_url = retrieve_and_store_streetview_image(place_id, lat, lng)

    property = Property.objects.create(
        sale_date=sale_date,
        raw_address=address,
        formatted_address=geocode_result["formatted_address"],
        county=county,
        neighborhood=_get_address_component(geocode_result, "neighborhood"),
        locality=_get_address_component(geocode_result, "locality"),
        sublocality=_get_address_component(geocode_result, "sublocality"),
        premise=_get_address_component(geocode_result, "premise"),
        subpremise=_get_address_component(geocode_result, "subpremise"),
        postal_code=_get_address_component(geocode_result, "postal_code"),
        postal_town=_get_address_component(geocode_result, "postal_town"),
        route=_get_address_component(geocode_result, "route"),
        price=price,
        description=description,
        lat=lat,
        lng=lng,
        stree_view_image_url=stree_view_image_url,
        digest=property_digest,
    )

    index_object(property=property)


def _get_address_component(geocode_result: Dict[str, Any], type: str) -> Optional[str]:
    for address_component in geocode_result["address_components"]:
        if type in address_component["types"]:
            return address_component["long_name"]
    return None
