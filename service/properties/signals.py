import logging
from typing import Type

from algoliasearch.search_client import SearchClient
from django.db.models.signals import post_save
from django.dispatch import receiver
from ppr.settings import ALGOLIA_API_KEY
from ppr.settings import ALGOLIA_APP_ID
from ppr.settings import ALGOLIA_PROPERTIES_INDEX_NAME
from properties.models import Property

algolia_client = SearchClient.create(ALGOLIA_APP_ID, ALGOLIA_API_KEY)
algolia_properties_index = algolia_client.init_index(ALGOLIA_PROPERTIES_INDEX_NAME)
logger = logging.getLogger("ppr.properties.signals")


@receiver(post_save, sender=Property)
def on_property_post_save(sender: Type[Property], instance: Property, created: bool, **kwargs):
    try:
        algolia_object = {
            "objectID": instance.id,
            "area": instance.area,
            "county": instance.county,
            "description": instance.description,
            "formatted_address": instance.formatted_address,
            "house": instance.house,
            "latitude": instance.latitude,
            "locality": instance.locality,
            "location_type": instance.location_type,
            "longitude": instance.longitude,
            "neighborhood": instance.neighborhood,
            "postal_code": instance.postal_code,
            "price": instance.price,
            "raw_address": instance.raw_address,
            "region": instance.region,
            "sale_date": instance.sale_date.strftime("%x"),
            "street": instance.street,
        }
        algolia_properties_index.save_object(algolia_object)
    except Exception:
        logger.exception("Error saving Algolia object [%s]", algolia_object)
