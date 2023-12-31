import pytest
from CS50_17_Calculator import square

def test_square_positive():
    assert square(2) == 4
    assert square(3) == 9
    assert square(25) == 625

def test_square_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_square_zero():
    assert square(0) == 0

# For passing string as a input in "x" in "CS50_17_Calculator.py" (PS ---> we've removed int from x)
def test_square_str():
    with pytest.raises(TypeError):
        square("cat")

# We'll run this program by using "pytest test_calculator1.py" in the terminal
