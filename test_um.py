from um import count

def test_um():
    assert count("hello um, my mame is um Teresa") == 2
    assert count("um, thanks for the album") == 1
    assert count("Um...thank you") == 1