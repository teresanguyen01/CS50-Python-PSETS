from twttr import shorten

def test_shorten_empty():
    assert shorten("") == ""
    assert shorten("Hello, World!") == "Hll, Wrld!"
    assert shorten("12345") == "12345"

