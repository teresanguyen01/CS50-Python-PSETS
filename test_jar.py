from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.cookies == 0

    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.cookies == 0

    with pytest.raises(ValueError):
        Jar(-1)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(5)

    jar.deposit(2)
    assert str(jar) == "🍪🍪"


def test_withdraw():
    jar = Jar(3)

    jar.deposit(2)
    jar.withdraw(1)

    assert str(jar) == "🍪"