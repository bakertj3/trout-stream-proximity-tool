from src.stream_data import load_data, streams_in_county, find_nearest_stream

def test_can_load_class_a_stream_data():
    """Verify that PA Class A stream GIS data can be loaded via GeoPandas"""
    # Arrange
    result_data = load_data()

    # Assert
    assert result_data is not None
    assert len(result_data) > 0
    assert 'geometry' in result_data.columns

def test_dataset_has_county_data_column():
    """Verify that PA Class A stream data contains county column"""
    # Arrange
    result_data = load_data()

    # Assert
    assert 'COUNTY_NAM' in result_data.columns

def test_can_filter_dataset_by_column():
    
    """Verify that PA Class A stream data can be filtered by county"""
     # Arrange
    result_data = load_data()
    county_data = streams_in_county(result_data, "Centre")

    assert county_data is not None
    assert len(county_data) < len(result_data)

def test_find_nearest_stream_to_point():
    """Try to find the nearest stream to State College"""
    # Arrange
    stream_data = load_data()
    centre_streams = streams_in_county(stream_data,"Centre")
    lat, lng = 40.7934, -77.8600 # State College, PA

    # Act
    nearest_stream, distance_miles = find_nearest_stream(centre_streams, lat, lng)

    # Assert
    assert nearest_stream is not None
    assert distance_miles > 0
    assert distance_miles < 50
    print(f"Nearest stream: {distance_miles:.2f} miles") #for debugging
    print(f"Nearest stream name: {nearest_stream.WtrName}")
    