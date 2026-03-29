import folium
import shapely

m = folium.Map(location=[40.9, -77.7])
marker = folium.Marker([40.9, -77.7])
marker.add_to(m)

print(dir(m))
print(type(m._children))
print(len(m._children))
print(m._children.keys())

coords = [[40.9, -77.7], [40.8, -77.6]]
line = folium.PolyLine(locations=coords)
print(dir(line))
print(line.locations)

line_a = shapely.LineString([[-75.52157326674316, 40.83175029368788], [-75.52206472890627, 40.83185482468983], [-75.52267926711609, 40.832074695709515]])
line_b = shapely.LineString([[-75.58578196194792, 40.859098227585946], [-75.58563196190089, 40.85910822759347], [-75.58549196185758, 40.85912822760267]])
stream = shapely.MultiLineString(lines=[line_a, line_b])

print(f"map_bounds before: {m.get_bounds()}")
#new_bounds = m.fit_bounds(map_bounds)
#stream_bounds = stream.get_bounds()
for l in stream.geoms:
    #l.add_to(m)
    print(f"stream bounds = {l.bounds}")
print(f"map_bounds after: {m.get_bounds()}")
#print(f"map bounds = {map_bounds}")
#print(f"new_bounds = {new_bounds}")

tooltip = folium.Tooltip("this tooltip")
print(type(tooltip))

popup = folium.Popup("<h2>This is my fantatstic pop up!</h2>")
result = dir(popup.html._children.values)
print(result)