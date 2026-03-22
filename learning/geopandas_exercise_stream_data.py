import src.stream_data as stream
import src.address_geocode as geocode
import shapely

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



# looking for streams with multiline geometry:
stream_geometry = stream_data.geometry
multline_streams = stream_geometry[shapely.get_num_geometries(stream_geometry) > 1].head(1).index
multi_stream = stream_data.iloc[multline_streams] #Kunkletown, PA - Hunter Creek
print(multi_stream)
print(multi_stream["WtrName"])




