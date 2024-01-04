from io import BytesIO
from typing import Any
from typing import Dict
from typing import Optional

import boto3
import googlemaps
import requests
from algoliasearch.search_client import SearchClient
from ppr.settings import ALGOLIA_API_KEY
from ppr.settings import ALGOLIA_APP_ID
from ppr.settings import AWS_ACCESS_KEY
from ppr.settings import AWS_ACCESS_KEY_ID
from ppr.settings import GOOGLE_MAPS_API_KEY
from ppr.settings import S3_STREET_VIEW_IMAGES_BUCKET_NAME
from ppr.settings import S3_STREET_VIEW_IMAGES_BUCKET_URL

from .models import Property

gmaps_client = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)
algolia_client = SearchClient.create(ALGOLIA_APP_ID, ALGOLIA_API_KEY)
session = boto3.session.Session(aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_ACCESS_KEY)
s3_client = session.client(service_name="s3")


def get_geocode_by_address(address: str, county: str, postal_code: Optional[str]) -> Dict[str, Any]:
    """
    Retrieves the geocode for a given address, county, and postal code.

    Args:
        address (str): The address to retrieve the geocode for.
        county (str): The county of the address.
        postal_code (Optional[str]): The postal code of the address.

    Returns:
        Dict[str, Any]: The geocode result for the given address, or None if no result is found.
    """
    geocode_result = gmaps_client.geocode(
        address=address,
        components={
            "administrative_area": county,
            "country": "IE",
            "postal_code": postal_code,
        },
    )
    return geocode_result[0] if geocode_result else None


def retrieve_and_store_streetview_image(place_id: str, lat: str, lng: str) -> str:
    """
    Retrieves and stores a static street view map for a given place_id.

    Args:
        place_id (str): The place ID of the location.
        lat (str): The latitude of the location.
        lng (str): The longitude of the location.

    Returns:
        str: The URL of the stored street view image.
    """
    params = {
        "key": GOOGLE_MAPS_API_KEY,
        "location": f"{lat},{lng}",
        "size": "600x600",
    }
    response = requests.get("https://maps.googleapis.com/maps/api/streetview", params=params, timeout=30)
    response.raise_for_status()
    content = BytesIO(response.content)
    object_key = f"{place_id}/streetview.jpg"
    s3_client.upload_fileobj(Fileobj=content, Bucket=S3_STREET_VIEW_IMAGES_BUCKET_NAME, Key=object_key)
    return f"{S3_STREET_VIEW_IMAGES_BUCKET_URL}/{object_key}"


def index_object(property: Property):
    """
    Indexes a property object in Algolia.

    Args:
        property (Property): The property object to be indexed.

    Returns:
        None
    """
    index = algolia_client.init_index("properties")
    index.save_object(
        {
            "objectID": property.digest,
            "place_id": property.place_id,
            "sale_date": property.sale_date.strftime("%x"),
            "county": property.county,
            "formatted_address": property.formatted_address,
            "price": property.price,
            "description": property.description,
            "locality": property.locality,
            "neighborhood": property.neighborhood,
            "postal_code": property.postal_code,
            "postal_town": property.postal_town,
            "route": property.route,
            "sublocality": property.sublocality,
            "latitude": property.lat,
            "longitude": property.lng,
            "premise": property.premise,
            "subpremise": property.subpremise,
            "stree_view_image_url": property.stree_view_image_url,
        }
    )
