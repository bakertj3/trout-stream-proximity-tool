"""test_app.py"""
from streamlit.testing.v1 import AppTest
from unittest.mock import patch

def test_app_has_address_input_field():
    # Arrange / # Act
    at = AppTest.from_file("../src/app.py").run()
    address_input = at.text_input[0]

    # Act
    assert address_input != None

def test_app_has_address_submit_button():
    # Arrange / # Act
    at = AppTest.from_file("../src/app.py").run()
    address_button = at.button[0]

    # Assert
    assert address_button != None

def test_app_info_text_not_displayed_before_button_click():
    # Arrange / # Act
    at = AppTest.from_file("../src/app.py").run()
    markdown_elements = at.get("markdown")

    # Assert
    assert len(markdown_elements) == 0

def test_app_info_text_displayed_after_button_click():
    # Arrange
    at = AppTest.from_file("../src/app.py").run()
    address = "State College, PA"
    address_input = at.text_input[0]
    address_input.set_value(address)
    address_button = at.button[0]

    # Act
    address_button.click().run()
    result_label = at.markdown[0]

    # Assert
    assert result_label != None

# After page reloads, Address is not blank, and submit button clicked, the map should be generated and displayed
@patch('src.proximity_map.generate_proximity_map')
@patch('src.proximity_analyzer.return_closest_stream')
def test_app_displays_map_with_successful_address_submission(mock1,mock2):
    # Arrange
    at = AppTest.from_file("../src/app.py").run()
    address = "State College, PA"
    address_input = at.text_input[0]
    address_input.set_value(address)
    address_button = at.button[0]

    # Act
    address_button.click().run()

    # Assert
    assert mock1.call_count == 1   
    assert mock2.call_count == 1

# After submit button clicked, functions are not called if address field is blank
@patch('src.proximity_map.generate_proximity_map')
@patch('src.proximity_analyzer.return_closest_stream')
def test_app_blank_address_does_not_call_map_functions(mock1,mock2):
    # Arrange
    at = AppTest.from_file("../src/app.py").run()
    address_button = at.button[0]

    # Act
    address_button.click().run()

    # Assert
    assert mock1.call_count == 0   
    assert mock2.call_count == 0

def test_app_has_title_displayed():
    # Arrange
    at = AppTest.from_file("../src/app.py").run()

    # Act
    result = at.title[0].value

    # Assert
    assert result == "Trout Stream Proximity Tool"
