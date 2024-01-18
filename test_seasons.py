import pytest
from seasons import seasons_function

#def test_seasons_function(): 
   #assert seasons_function("2019-12-01") == "Two million, one hundred and fifty-two thousand, eight hundred minutes"
    
def test_invalid_format(): 
    with pytest.raises(ValueError):
        seasons_function("invalid input")