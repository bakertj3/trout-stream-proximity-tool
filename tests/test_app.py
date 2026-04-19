"""test_app.py"""
from streamlit.testing.v1 import AppTest
from unittest.mock import patch
import streamlit_folium
import folium
import src

def test_app_has_address_input_field():
    at = AppTest.from_file("../src/app.py").run()
    address_input = at.text_input[0]
    assert address_input != None

def test_app_has_address_submit_button():
    at = AppTest.from_file("../src/app.py").run()
    address_button = at.button[0]
    assert address_button != None

# After page reloads after submit button clicked, the map should be generated and displayed
@patch('src.proximity_map.generate_proximity_map')
def test_app_displays_map_with_successful_address_submission(mock):
    at = AppTest.from_file("../src/app.py").run()
    address = "State College, PA"
    address_input = at.text_input[0]
    address_input.set_value(address)
    address_button = at.button[0]
    address_button.click().run()
    print(f"at = {at}")
    assert mock.call_count == 1   
