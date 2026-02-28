import geopandas as gpd
from geodatasets import get_path

def test_can_load_nybb_data():
    """Verify GeoPandas can load sample GIS data"""
    path = get_path("nybb")
    gdf = gpd.read_file(path)
    assert len(gdf) == 5
    assert "BoroName" in gdf.columns