import src.stream_data as stream
import src.address_geocode as geocode

result = geocode.address_geocode("Lock Haven, PA")
print(result)
stream_data = stream.load_data()
nearest_stream, distance = stream.find_nearest_stream(stream_data, result["lat"], result["lng"])

stream_geometry = nearest_stream["geometry"]
print("----- NEAREST STREAM - Geometry -----")
print(stream_geometry)
print("----- NEAREST STREAM - Geometry - TYPE -----")
print(type(stream_geometry))

print(stream_geometry.geom_type)