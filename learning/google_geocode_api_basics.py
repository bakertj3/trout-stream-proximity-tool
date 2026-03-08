import googlemaps
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_MAPS_API_KEY")
gmaps = googlemaps.Client(key=api_key)

result = gmaps.geocode("State College, PA")

print(result)

location = result[0]["geometry"]["location"]

lat = location["lat"]
lng = location["lng"]

print(lat, lng)

result = gmaps.geocode("asdasdfasdfadf")

location2 = result[0]["geometry"]["location"]

print(location2)