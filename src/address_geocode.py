import googlemaps
import os
from dotenv import load_dotenv

def address_geocode(input_address):
    load_dotenv()
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    gmaps = googlemaps.Client(key=api_key)
    
    result = gmaps.geocode(input_address)

    if result == []:
        raise ValueError("Invalid Address")
    
    return result