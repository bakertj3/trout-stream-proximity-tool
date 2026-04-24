import src.proximity_analyzer as prox
from shapely.geometry.base import BaseGeometry


def test_return_closest_stream_should_have_dictionary_values():
    # Arrange
    address = "Harrisburg, PA"

    # Act
    result = prox.return_closest_stream(address)

    # Assert
    assert result["address_coords"] != None
    assert result["nearest_stream_name"] != ""
    assert result["nearest_stream_distance_miles"] > 0
    assert result["stream_geometry"] is not None

def test_return_closest_stream_should_have_latlng_keys_and_nonzero_values():
    # Arrange
    address = "Harrisburg, PA"

    # Act
    result = prox.return_closest_stream(address)

    # Assert
    assert list(result["address_coords"].keys()) == ["lat", "lng"]
    assert result["address_coords"]["lat"]
    assert isinstance(result["address_coords"]["lat"], float)
    assert isinstance(result["address_coords"]["lng"], float)

def test_return_closest_stream_name_should_have_non_empty_value():
    # Arrange
    address = "Harrisburg, PA"
    
    # Act
    result = prox.return_closest_stream(address)

    # Assert
    assert len(result["nearest_stream_name"]) > 0

def test_return_closest_stream_different_addresses_should_have_different_results():
    # Arrange
    address1 = "Harrisburg, PA"
    address2 = "Pittsburgh, PA"
    
    # Act
    result1 = prox.return_closest_stream(address1)
    result2 = prox.return_closest_stream(address2)

    # Assert
    assert result1["nearest_stream_name"] != result2["nearest_stream_name"]

def test_return_closest_stream_should_return_geometry_for_stream_mapping():
    # Arrange
    address = "Lock Haven, PA"

    # Act
    result = prox.return_closest_stream(address)

    # Assert
    assert isinstance(result["stream_geometry"], BaseGeometry)

def test_return_closest_stream_should_return_percent_on_public_land():
    # Arrange
    address = "Galeton, PA"

    # Act
    result = prox.return_closest_stream(address)

    # Assert
    assert result["percent_on_public_land"] != None

def test_return_closest_stream_should_return_input_address_in_result():
    # Arrange
    address = "Coudersport, PA"

    #Act
    result = prox.return_closest_stream(address)

    # Assert
    assert result["address"] == address