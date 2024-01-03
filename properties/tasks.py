import csv
import re
from datetime import datetime, timedelta

import requests
from celery import shared_task

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
            Property.objects.update_or_create(
                sale_date=datetime.strptime(property_data[0], "%d/%m/%Y").date(),
                formatted_address=property_data[1],
                county=county,
                defaults={
                    "eircode": property_data[3],
                    "price": re.sub(r"[^\d.]", "", property_data[4]),
                    "description": property_data[7],
                },
            )
