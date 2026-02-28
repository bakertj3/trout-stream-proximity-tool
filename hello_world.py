import geopandas as gpd
from geodatasets import get_path
import matplotlib.pyplot  as plt


path_to_data = get_path("nybb")
gdf = gpd.read_file(path_to_data)

#gdf.to_file("test_1.geojson", driver="GeoJson")

gdf = gdf.set_index("BoroName")
gdf["area"] = gdf.area
gdf["boundary"] = gdf.boundary
gdf["centroid"] = gdf.centroid

print(gdf["area"])
print(gdf["boundary"])
print(gdf["centroid"])
gdf.plot("area", legend=True)
plt.show()
