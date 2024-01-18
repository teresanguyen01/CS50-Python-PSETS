import pytest
from fuel import convert, gauge

def main():
    test_gauge()
    test_convert_invalid()

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(50) == f"{50}%"
    assert convert("1/2") == 50.0

def test_convert_invalid():
    with pytest.raises(ZeroDivisionError):
        convert("4/0") 
    with pytest.raises(ValueError):
        convert("booger")
        convert("s/d")
        convert("s/100")
        convert("-5/10")
        convert("1.5/10")

if __name__ == "__main__":
    main()
