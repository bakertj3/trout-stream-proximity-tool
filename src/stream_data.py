import geopandas as gpd
from shapely.geometry import Point

def load_data():
    stream_data = gpd.read_file("data/Class A Trout Streams.geojson")
    return stream_data

def streams_in_county(stream_data, county_name):
    return stream_data[stream_data["COUNTY_NAM"].str.contains(county_name)]

def find_nearest_stream(streams, lat, lng):
    """find_nearest_stream to a Lat/Lng point and return distance in miles.
    
    Uses proper geodesic distance calc by reprojecting to UTM.
    """
    # create point in WSG84
    point_wgs84 = Point(lng, lat)
    point_gdf = gpd.GeoDataFrame(geometry=[point_wgs84], crs="EPSG:4326")

    # Reproject data to UTM zone 18N (for PA)
    streams_utm = streams.to_crs("EPSG:32618")
    point_utm = point_gdf.to_crs("EPSG:32618")

    # Calculate distance in meters
    streams_utm = streams_utm.copy()
    streams_utm["distance_m"] = streams_utm.geometry.distance(point_utm.geometry[0])

    # find nearest
    nearest_index = streams_utm["distance_m"].idxmin()
    nearest_stream = streams.loc[nearest_index] # original, not projected
    distance_meters = streams_utm["distance_m"].min()

    # convert distance to miles
    distance_miles = distance_meters * 0.000621371

    return nearest_stream, distance_miles


    