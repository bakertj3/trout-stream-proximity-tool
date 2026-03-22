import folium
import shapely
import src.address_geocode as geocode
import src.proximity_analyzer as analyzer

def generate_proximity_map(address):
    address_coords = geocode.address_geocode(address)
    mappable_address_coords = [address_coords["lat"],address_coords["lng"]]

    m = folium.Map(mappable_address_coords)

    address_marker = folium.Marker(location=mappable_address_coords)
    address_marker.add_to(m)

    closest_stream = analyzer.return_closest_stream(address)
    stream_geometry = closest_stream["stream_geometry"]
    num_geoms = shapely.get_num_geometries(stream_geometry)
    print(f"num_geoms = {num_geoms}")
    for i in range(num_geoms):
        geometry = shapely.get_geometry(stream_geometry,i)
        coord_set = geometry.coords
        print(coord_set)
        # need to reverse stream coords because geojson coords are stored [lng, lat]
        # folium needs coords in [lat, lng] order
        mappable_stream_coords = []
        for point in coord_set:
            point_coords = list(point)
            rev_coords = point_coords[::-1]
            mappable_stream_coords.append(rev_coords)

        stream_line = folium.PolyLine(locations=mappable_stream_coords)

        stream_line.add_to(m)

    return m