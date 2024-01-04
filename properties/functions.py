import googlemaps

from ppr.settings import GOOGLE_MAPS_API_KEY

gmaps_client = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)


def get_geocode(address: str, county: str):
    """
    Retrieves the geocode for a given address and county.

    Args:
        address (str): The address to retrieve the geocode for.
        county (str): The county of the address.

    Returns:
        geocode_result: The geocode result for the given address and county.
    """
    print(f"Retrieving geo code for address: {address} ...")
    geocode_result = gmaps_client.geocode(
        address=address, components={"administrative_area": county, "country": "IE"}
    )
    print(
        f"Geo code result for address {address}: {geocode_result}",
        address,
        geocode_result,
    )
    return geocode_result


def get_place(place_id: str):
    """
    Retrieves place details for a given place_id.

    Args:
        place_id (str): The ID of the place to retrieve details for.

    Returns:
        dict: A dictionary containing the place details.
    """
    print(f"Retrieving place details for place_id: {place_id}")
    place = gmaps_client.place(place_id)
    print(f"Place details for place_id {place_id}: {place}")
    return place
