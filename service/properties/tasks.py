import csv
import decimal
import hashlib
import io
import logging
import re
from datetime import date
from datetime import datetime
from datetime import timedelta
from typing import Optional

import requests
from celery import shared_task
from ppr.settings import PROPERTY_PRICE_REGISTER_BASE_URL
from properties.models import County
from properties.models import Property
from properties.utils import geocode_address

logger = logging.getLogger("ppr.properties.tasks")


@shared_task(name="load_properties")
def load_properties(lookback_months: int = 1):
    """
    Load properties for a given number of lookback months for all Irish counties.

    Args:
        lookback_months (int): The number of months to look back.
    """
    logger.info("Loading properties with [%s] lookback months ...", lookback_months)
    for month in range(lookback_months):
        sale_date = datetime.today() - timedelta(days=30 * month)
        for county in County.values:
            load_properties_for_county_and_date.delay(
                county=county,
                month=f"{sale_date:%m}",
                year=f"{sale_date:%Y}",
            )


@shared_task(name="load_properties_for_county_and_date")
def load_properties_for_county_and_date(county: County, month: str, year: str):
    """
    Load properties for a specific county and date from the Property Price Register.

    Args:
        county (County): The county for which to retrieve properties.
        month (str): The month of the properties.
        year (str): The year of the properties.

    Raises:
        Exception: If there is an error retrieving the properties.
    """
    try:
        logger.info("Retrieving properties for county [%s] and date [%s:%s] ...", county, year, month)
        csv_file_name = f"PPR-{year}-{month}-{county}.csv"
        url = f"{PROPERTY_PRICE_REGISTER_BASE_URL}/Downloads/{csv_file_name}/$FILE/{csv_file_name}"
        response = requests.get(url=url, timeout=30)
        response.raise_for_status()
        response.encoding = "Windows-1252"
        csv_content = io.StringIO(response.text.strip())
        reader = csv.DictReader(csv_content, delimiter=",")
        for row in reader:
            load_property.delay(
                sale_date=datetime.strptime(row["Date of Sale (dd/mm/yyyy)"], "%d/%m/%Y").date(),
                address=row["Address"],
                county=county,
                price=re.sub(r"[^\d.]", "", row["Price (€)"]),
                postal_code=row["Eircode"],
                description=row["Description of Property"],
            )
    except Exception:
        logger.exception("Error retrieving properties for county [%s] and date [%s:%s]", county, year, month)


@shared_task(name="load_property")
def load_property(
    sale_date: date,
    address: str,
    county: County,
    price: str,
    postal_code: Optional[str],
    description: Optional[str],
):
    """
    Loads a property into the system.

    Args:
        sale_date (date): The date of the property sale.
        address (str): The address of the property.
        county (County): The county of the property.
        price (str): The price of the property.
        postal_code (Optional[str]): The postal code of the property (optional).
        description (Optional[str]): The description of the property (optional).
    """
    logger.info("Retrieving properties for county [%s] and address [%s] ...", county, address)

    property_digest = hashlib.md5(f"{sale_date.isoformat()}#{address}#{price}".encode(), usedforsecurity=False).hexdigest()
    if Property.objects.filter(digest=property_digest).exists():
        logger.warning("Property with digest [%s] already exists", property_digest)
        return

    geocode_result = geocode_address(address=address)
    if geocode_result is None:
        logger.error("No geocode found for address [%s]. The property will be saved with basic details.", address)
        Property.objects.create(
            county=county,
            description=description,
            digest=property_digest,
            postal_code=postal_code,
            price=price,
            raw_address=address,
            sale_date=sale_date,
        )
        return

    Property.objects.create(
        area=geocode_result.get("area"),
        county=county,
        description=description,
        digest=property_digest,
        formatted_address=geocode_result.get("address"),
        house=geocode_result.get("house"),
        latitude=decimal.Decimal(geocode_result["location"]["lat"]).quantize(decimal.Decimal(".000001")),
        locality=geocode_result.get("locality"),
        location_type=geocode_result.get("location_type"),
        longitude=decimal.Decimal(geocode_result["location"]["lng"]).quantize(decimal.Decimal(".000001")),
        neighborhood=geocode_result.get("neighborhood"),
        postal_code=postal_code if postal_code else geocode_result.get("postal_code"),
        price=price,
        raw_address=address,
        region=geocode_result.get("region"),
        sale_date=sale_date,
        street=geocode_result.get("street"),
    )
