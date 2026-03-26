from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="yt_locator")

def get_coordinates(location: str):
    loc = geolocator.geocode(location)
    if not loc:
        raise ValueError("Location not found")
    return loc.latitude, loc.longitude