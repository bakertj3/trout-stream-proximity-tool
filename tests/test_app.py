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


@patch('src.proximity_map.generate_proximity_map')
def test_app_calls_proximity_map_function_when_button_clicked(mock):
    at = AppTest.from_file("../src/app.py").run()
    address = "State College, PA"
    address_input = at.text_input[0]
    address_input.set_value(address)
    address_button = at.button[0]
    address_button.click().run()
    assert mock.call_count == 1

@patch('src.app.display_map')
@patch('src.proximity_map.generate_proximity_map')
def test_app_displays_map_with_successful_address_submission(mock1, mock2):
    at = AppTest.from_file("../src/app.py").run()
    address = "State College, PA"
    address_input = at.text_input[0]
    address_input.set_value(address)
    address_button = at.button[0]
    address_button.click().run()
    print(f"at = {at}")
    assert mock1.call_count == 1


 
    
