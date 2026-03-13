import src.address_geocode as geocode
import src.stream_data as stream

def return_closest_stream(address):
    result = dict()

    # geocode input address
    address_coords = geocode.address_geocode(address)
    result["address_coords"] = address_coords

    # find nearest stream
    stream_data = stream.load_data()
    nearest_stream, nearest_dist = stream.find_nearest_stream(stream_data, address_coords["lat"], address_coords["lng"])

    result["nearest_stream_name"] = nearest_stream["WtrName"]
    result["nearest_stream_distance_miles"] = nearest_dist
    result["stream_geometry"] = {"type": "", "geometry":[]}
    return result