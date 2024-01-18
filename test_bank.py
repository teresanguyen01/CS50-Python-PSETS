from bank import value

def main():
    test_checks()

def test_checks():
    assert value("hello") == 0
    assert value("whatever") == 100
    assert value("hey") == 20
    assert value("Hello") == 0
    assert value("hello") == 0 

if __name__ == "__main__":
    main()