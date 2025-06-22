import pytest
from src.calculator import add, subtract, multiply, divide

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -2) == -3

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(4, 3) == 12

def test_divide_normal():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_add_floats():
    assert add(0.1, 0.2) == pytest.approx(0.3)

def test_subtract_floats():
    assert subtract(0.3, 0.1) == pytest.approx(0.2)

def test_multiply_zero():
    assert multiply(0, 100) == 0

def test_divide_negative():
    assert divide(-10, 2) == -5
