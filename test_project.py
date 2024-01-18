from project import convert_to_number, convert_to_numerals, random_roman

def test_convert_to_number():
    assert convert_to_number("V") == 5
    assert convert_to_number("I") == 1

def test_convert_to_numerals(): 
    assert convert_to_numerals(5) == "V"
    assert convert_to_numerals(1) == "I"