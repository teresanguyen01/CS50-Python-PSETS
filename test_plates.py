from plates import is_valid

def main():
    test_alphabet()
    test_length()
    test_numberplace()
    test_zero()
    test_alphanumeric()


def test_alphabet():
    assert is_valid("23") == False
    assert is_valid("AA") == True

def test_length():
    assert is_valid("A") == False
    assert is_valid("AA3") == True

def test_numberplace():
    assert is_valid("AA323") == True
    assert is_valid("AA723A") == False

def test_zero():
    assert is_valid("AA023") == False

def test_alphanumeric():
    assert is_valid("AA.23") == False

if __name__ == "__main__":
    main()