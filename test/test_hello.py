from hello import hello


def test_hello_argument():
    assert hello("Ganesh") == "Hello, Ganesh"

def test_hello_default():
    assert hello() == "Hello, World"
