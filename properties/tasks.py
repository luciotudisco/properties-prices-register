from datetime import datetime, timedelta

import requests
from celery import shared_task

BASE_URL = "https://www.propertypriceregister.ie/website/npsra/ppr/npsra-ppr.nsf"


@shared_task(name="load_properties")
def load_properties():
    load_date = datetime.now() - timedelta(days=10)
    county = "Dublin"
    csv_file_name = f"PPR-{load_date.year}-{load_date.month}-{county}.csv"
    url = f"{BASE_URL}/Downloads/{csv_file_name}/$FILE/{csv_file_name}"
    response = requests.get(url, verify=False, timeout=30)  # nosec
    response.raise_for_status()
    rows = response.text.splitlines()
    print(rows)
