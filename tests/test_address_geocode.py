from src.address_geocode import address_geocode
import pytest

def test_invalid_address_should_throw_value_error():
    """Verify that an invalid address should throw ValueError"""
    failing_address = "asdfasdfasdfasdf"
    with pytest.raises(ValueError):
        address_geocode(failing_address)

def test_valid_address_should_return_geocoded_object():
    """Verify that a valid address successfully returns lat/lng results from the dictionary result"""
    
    valid_address = "4200 Penn Ave, Pittsburgh, PA"
    result = address_geocode(valid_address)
    
    key_result = list(result.keys())
    expected_keys = ["lat", "lng"]

    assert key_result == expected_keys
    assert type(result["lat"]) == float
    assert type(result["lng"]) == float
    assert result["lat"] >= 39 and result["lat"] <=43
    assert result["lng"] >= -81 and result["lng"] <= -74

def test_non_PA_address_should_throw_value_error():
    """Verify that address_geocode() rejects non-PA addresses by returning a ValueError"""
    
    non_pa_address = "San Diego, CA"
    with pytest.raises(ValueError):
        address_geocode(non_pa_address)

    


