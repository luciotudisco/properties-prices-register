import logging
import sys
import time
from datetime import date

import requests
from algoliasearch.search_client import SearchClient

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger("scripts.reindex")


def reindex_properties(algolia_app_id: str, algolia_api_key: str, algolia_ndex_name: str) -> None:
    """
    Reindexes all properties in Algolia in batches.

    Args:
        algolia_app_id (str): The Algolia application ID.
        algolia_api_key (str): The Algolia API key.
        algolia_ndex_name (str): The name of the Algolia index.

    Returns:
        None
    """
    algolia_client = SearchClient.create(algolia_app_id, algolia_api_key)
    algolia_properties_index = algolia_client.init_index(algolia_ndex_name)
    url = "https://api.irishpropertiesprices.com/v1/properties/"
    num_properties = 0
    while True:
        response = requests.get(url=url, timeout=30)
        response.raise_for_status()
        json_response = response.json()
        properties = json_response["results"]
        algolia_objects = []
        for property in properties:
            sale_date = date.fromisoformat(property.get("sale_date"))
            algolia_objects.append(
                {
                    "objectID": property.get("id"),
                    "area": property.get("area"),
                    "county": property.get("county"),
                    "description": property.get("description"),
                    "formatted_address": property.get("formatted_address"),
                    "house": property.get("house"),
                    "latitude": property.get("latitude"),
                    "locality": property.get("locality"),
                    "location_type": property.get("location_type"),
                    "longitude": property.get("longitude"),
                    "neighborhood": property.get("neighborhood"),
                    "postal_code": property.get("postal_code"),
                    "price": float(property.get("price")),
                    "raw_address": property.get("raw_address"),
                    "region": property.get("region"),
                    "sale_date": time.mktime(sale_date.timetuple()),
                    "sale_year": sale_date.year,
                    "street": property.get("street"),
                    "property_type": property.get("property_type"),
                }
            )
        algolia_properties_index.save_objects(algolia_objects)
        num_properties += len(algolia_objects)
        logger.info("[%s] properties saved", num_properties)
        has_next = json_response["next"] is not None
        if not has_next:
            break
        url = json_response["next"]
    logger.info("Reindexing complete. [%s] properties saved", num_properties)


if __name__ == "__main__":
    algolia_app_id = input("Algolia app id: ")
    algolia_app_key = input("Algolia app key: ")
    algolia_index_name = input("Algolia index name: ")
    reindex_properties(algolia_app_id, algolia_app_key, algolia_index_name)
