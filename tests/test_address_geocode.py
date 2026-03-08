from src.address_geocode import *
import googlemaps as gmap
import pytest

def test_invalid_address_should_throw_value_error():
    failing_address = "asdfasdfasdfasdf"
    with pytest.raises(ValueError):
        address_geocode(failing_address)
