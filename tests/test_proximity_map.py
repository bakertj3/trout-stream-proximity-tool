from src import proximity_map as prox_map, proximity_analyzer as prox, address_geocode as geocode
import shapely
import folium


# Arrange
test_data_single = dict()
test_data_single["address"] = "Bellefonte, PA"
test_data_single["address_coords"] = {"lat": 40.91339430000001, "lng": -77.7783348}
test_data_single["stream_geometry"] = shapely.LineString([[-77.781, 40.912], [-77.781, 40.912], [-77.781, 40.913], [-77.782, 40.913]])
test_data_single["nearest_stream_name"] = "Spring Creek"
test_data_single["nearest_stream_distance_miles"] = 15
test_data_single["percent_on_public_land"] = 0.1

test_data_multi = dict()
line_a = shapely.LineString([[-75.52157326674316, 40.83175029368788], [-75.52206472890627, 40.83185482468983], [-75.52267926711609, 40.832074695709515]])
line_b = shapely.LineString([[-75.58578196194792, 40.859098227585946], [-75.58563196190089, 40.85910822759347], [-75.58549196185758, 40.85912822760267]])
test_data_multi["address"] = "Spruce Hollow Road, Kunkletown, PA"
test_data_multi["address_coords"] = {"lat": 40.809339, "lng": -77.083364}
test_data_multi["stream_geometry"] = shapely.MultiLineString(lines=[line_a, line_b])
test_data_multi["nearest_stream_name"] = "Hunter Creek"
test_data_multi["nearest_stream_distance_miles"] = 0.038
test_data_multi["percent_on_public_land"] = 0.00

def test_generate_stream_proximity_map_successfully_returns_map():
    # Act
    result = prox_map.generate_proximity_map(test_data_single)

    # Assert
    assert isinstance(result, folium.Map)

def test_generate_stream_proximity_map_is_centered_on_input_address():
    # Arrange
    # Act
    result = prox_map.generate_proximity_map(test_data_single)

    # Assert
    assert result.location == [test_data_single["address_coords"]["lat"],test_data_single["address_coords"]["lng"]]

def test_generate_stream_proximity_map_has_marker_at_input_address():
    # Arrange
    # Act
    result = prox_map.generate_proximity_map(test_data_single)

    # Assert
    assert len(result._children) > 0

    markers = [child for child in result._children.values()
               if isinstance(child, folium.Marker)]
    assert len(markers) == 1

def test_generate_stream_proximity_map_displays_closest_stream():
    # Arrange
    # Act
    result = prox_map.generate_proximity_map(test_data_single)

    stream_line = [child for child in result._children.values()
                if isinstance(child, folium.PolyLine)]

    # Assert
    assert len(stream_line) == 1

def test_generate_stream_proximity_map_stream_latitude_within_PA_bounds():
    # Arrange
    # Act
    result = prox_map.generate_proximity_map(test_data_single)

    stream_line = [child for child in result._children.values()
                   if isinstance(child, folium.PolyLine)][0]

    # Assert
    for coord in stream_line.locations:
        assert 39 <= coord[0] <= 43

def test_generate_stream_proximity_map_can_map_multi_linestrings():
    # Arrange
    # Act
    result = prox_map.generate_proximity_map(test_data_multi)

    stream_line = [child for child in result._children.values() 
                   if isinstance(child, folium.PolyLine)]

    # Assert
    assert len(stream_line) > 1

def test_generate_stream_proximity_map_stream_line_has_tooltip():
    # Arrange
    # Act
    result = prox_map.generate_proximity_map(test_data_multi)

    stream_line = [child for child in result._children.values() if isinstance(child, folium.PolyLine)]

    # Assert
    for stream in stream_line:
        assert len([tooltip for tooltip in stream._children.values() if isinstance(tooltip, folium.Tooltip)]) > 0

def test_generate_stream_proximity_map_stream_tooltip_contains_stream_name():
    # Arrange
    # Act
    result = prox_map.generate_proximity_map(test_data_multi)

    stream_line = [child for child in result._children.values() if isinstance(child, folium.PolyLine)]
    tool_tip = []
    for stream in stream_line:
        tool_tip.append([tooltip for tooltip in stream._children.values() if isinstance(tooltip, folium.Tooltip)])

    # Assert
    for item in tool_tip:
        assert test_data_multi["nearest_stream_name"] == item[0].text

def test_generate_stream_proximity_map_stream_line_when_clicked_displays_popup_with_stream_info():
    # Arrange
    # Act
    result = prox_map.generate_proximity_map(test_data_multi)

    stream_line = [child for child in result._children.values() if isinstance(child, folium.PolyLine)]
    
    popup = []
    for stream in stream_line:
        popup.append([popup for popup in stream._children.values() if isinstance(popup, folium.Popup)])

    # Assert
    # we want to make sure that there is a popup for each PolyLine in a Multiline geometry
    assert len(popup) > 1
    # verify that there is a popup for each Polyline within the Multline
    for item in popup:
        popup_html = item[0].html.render()
        assert test_data_multi["nearest_stream_name"] in popup_html
        assert str(test_data_multi["nearest_stream_distance_miles"]) in popup_html
        assert str(test_data_multi["percent_on_public_land"]) in popup_html

