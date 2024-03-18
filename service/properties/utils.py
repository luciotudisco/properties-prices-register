import logging
from typing import Any
from typing import Dict
from typing import Optional

import requests
from ppr.settings import GEOCODE_API_HOST
from ppr.settings import GEOCODE_API_KEY
from ppr.settings import GEOCODE_API_URL

logger = logging.getLogger("ppr.properties.utils")


def geocode_address(address: str) -> Optional[Dict[str, Any]]:
    """
    Geocode the given address.

    Args:
        address (str): The address to geocode.

    Returns:
        The geocode result for the given address, or None if no result is found.
    """
    try:
        logger.info("Retrieving geocode for address [%s] ...", address)
        response = requests.get(
            url=GEOCODE_API_URL,
            headers={"X-RapidAPI-Key": GEOCODE_API_KEY, "X-RapidAPI-Host": GEOCODE_API_HOST},  # nosec
            params={"address": address, "language": "en", "country": "IE"},
            timeout=5,
        )
        response.raise_for_status()
        json_response = response.json()
        geo_code_results = json_response.get("results", [])
        return geo_code_results[0] if geo_code_results else None
    except requests.RequestException as e:
        if e.response and e.response.status_code == 404:
            logger.warning("No geocode found for address [%s]", address)
            return None
        raise e
