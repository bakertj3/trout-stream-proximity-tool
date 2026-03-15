import folium
import src.address_geocode as geocode
import src.proximity_analyzer as prox

m = folium.Map(location=[40.7934, -77.8600]) # State College, PA

fly_shop_address = "2603 East College Avenue State College, PA 16801"
fly_shop_coords = geocode.address_geocode(fly_shop_address)

coords = list()
coords.append(fly_shop_coords["lat"])
coords.append(fly_shop_coords["lng"])

icon_spec = {"icon":"store", "prefix":"fa"}
icon = folium.Icon(**icon_spec)

fly_shop_marker = folium.Marker(
    location=coords, 
    tooltip="More Info", 
    popup="Fly Fisher's Paradise\n2603 East College Avenue\nState College, PA 16801", 
    icon=icon
)
fly_shop_marker.add_to(m)

nearest_stream = prox.return_closest_stream(fly_shop_address)
#print(nearest_stream)
coord_set = nearest_stream["stream_geometry"].coords
stream_bounds = nearest_stream["stream_geometry"].bounds
bounds_list = list(stream_bounds)
map_bounds = [[bounds_list[1],bounds_list[0]],[bounds_list[1], bounds_list[2]],[bounds_list[3], bounds_list[2]],[bounds_list[3], bounds_list[0]]]
stream_box = folium.Polygon(map_bounds, color="#DDD000")
stream_box.add_to(m)
print(map_bounds)

coords = []
for point in coord_set:
    point_list = list(point)
    rev_coords = point_list[::-1]
    coords.append(rev_coords)

stream_line = folium.PolyLine(locations=coords, color="#FF0000")
stream_line.add_to(m)
m.save("test_map.html")
