import pytest
from working import convert

def test_valid_conversion():
    assert convert("5 PM to 7 PM") == "17:00 to 19:00"

def test_edge_case_noon_and_midnight():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("invalid input")

def test_out_of_range_time():
    with pytest.raises(ValueError):
        convert("13 PM to 14 PM")
