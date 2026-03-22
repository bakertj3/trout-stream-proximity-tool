import folium

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