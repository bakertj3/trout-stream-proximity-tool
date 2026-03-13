import googlemaps
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_MAPS_API_KEY")
gmaps = googlemaps.Client(key=api_key)

def address_geocode(input_address):
    
    result = gmaps.geocode(input_address) 

    if result == []:
        raise ValueError("Invalid Address")
    
    location = result[0]["geometry"]["location"]
    
    if location["lat"] < 39 or location["lat"] > 43 or location["lng"] > -74 or location["lng"] < -81:
        raise ValueError("Address must be within Pennsylvania")
    
    return location