import folium
import shapely

def generate_proximity_map(closest_stream):
    address_coords = closest_stream["address_coords"]
    mappable_address_coords = [address_coords["lat"],address_coords["lng"]]

    m = folium.Map(mappable_address_coords)

    address_marker = folium.Marker(location=mappable_address_coords)
    address_marker.add_to(m)

    stream_geometry = closest_stream["stream_geometry"]
    stream_name = closest_stream["nearest_stream_name"]
    stream_distance = closest_stream["nearest_stream_distance_miles"]
    stream_percent_public_land = closest_stream["percent_on_public_land"]
    num_geoms = shapely.get_num_geometries(stream_geometry)
    for i in range(num_geoms):
        geometry = shapely.get_geometry(stream_geometry,i)
        coord_set = geometry.coords
        # need to reverse stream coords because geojson coords are stored [lng, lat]
        # folium needs coords in [lat, lng] order
        mappable_stream_coords = []
        for point in coord_set:
            point_coords = list(point)
            rev_coords = point_coords[::-1]
            mappable_stream_coords.append(rev_coords)

        stream_line = folium.PolyLine(locations=mappable_stream_coords)
        stream_line.add_to(m)

        tool_tip = folium.Tooltip(f"{stream_name}")    
        stream_line.add_child(tool_tip)

        pop_up = folium.Popup(f"<h2>Stream Name: {stream_name}</h2>\
                              <p>Distance from address: {stream_distance:.3f} miles<br />\
                                Percent on public land: {stream_percent_public_land}</p>")
        stream_line.add_child(pop_up)

    return m