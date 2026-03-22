from src import proximity_map as prox_map
import shapely
import folium


# Arrange
test_data = dict()
test_data["test_address"] = "Bellefonte, PA"
test_data["test_address_coords"] = [40.91339430000001,-77.7783348]
test_data["stream_geometry"] = shapely.LineString([[-77.781, 40.912], [-77.781, 40.912], [-77.781, 40.913], [-77.782, 40.913]])
line_a = shapely.LineString([[-75.52157326674316, 40.83175029368788], [-75.52206472890627, 40.83185482468983], [-75.52267926711609, 40.832074695709515]])
line_b = shapely.LineString([[-75.58578196194792, 40.859098227585946], [-75.58563196190089, 40.85910822759347], [-75.58549196185758, 40.85912822760267]])
test_data["multi_linestring"] = shapely.MultiLineString(lines=[line_a, line_b])
test_data["multi_linestring_address"] = "Spruce Hollow Road, Kunkletown, PA"

def test_generate_stream_proximity_map_successfully_returns_map():
    # Act
    result = prox_map.generate_proximity_map(test_data["test_address"])

    # Assert
    assert isinstance(result, folium.Map)

def test_generate_stream_proximity_map_is_centered_on_input_address():
    # Arrange
    address = test_data["test_address"]
    address_coords = test_data["test_address_coords"]

    # Act
    result = prox_map.generate_proximity_map(address)

    # Assert
    assert result.location == address_coords

def test_generate_stream_proximity_map_has_marker_at_input_address():
    # Arrange
    address = test_data["test_address"]

    # Act
    result = prox_map.generate_proximity_map(address)

    # Assert
    assert len(result._children) > 0

    markers = [child for child in result._children.values()
               if isinstance(child, folium.Marker)]
    assert len(markers) == 1

def test_generate_stream_proximity_map_displays_closest_stream():
    # Arrange
    address = test_data["test_address"]

    # Act
    result = prox_map.generate_proximity_map(address)

    # Assert
    stream_line = [child for child in result._children.values()
                   if isinstance(child, folium.PolyLine)]
    assert len(stream_line) == 1

def test_generate_stream_proximity_map_stream_latitude_within_PA_bounds():
    # Arrange
    address = test_data["test_address"]

    # Act
    result = prox_map.generate_proximity_map(address)

    print(result._children.values)
    stream_line = [child for child in result._children.values()
                   if isinstance(child, folium.PolyLine)][0]

    # Assert
    for coord in stream_line.locations:
        assert 39 <= coord[0] <= 43

def test_generate_stream_proximity_map_can_map_multi_linestrings():
    # Arrange
    address = test_data["multi_linestring_address"]

    # Act
    result = prox_map.generate_proximity_map(address)

    # Assert
    stream_line = [child for child in result._children.values()
                   if isinstance(child, folium.PolyLine)]
    assert len(stream_line) > 1

# map created
# coordinate reverse function?
# marker displayed on map
# map bounds encompass both stream and address (address in center of map window?)
# stream mapping can handle MultiLineString geometry
# stream line/marker - Displays Stream Info in tooltip?
