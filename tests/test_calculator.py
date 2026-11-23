import pytest

from src.calculator import add, divide, multiply, subtract


def test_add_with_positive_numbers():
    assert add(10, 5) == 15


def test_add_with_negative_numbers():
    assert add(-10, -5) == -15


def test_subtract_returns_zero_at_equal_values():
    assert subtract(7, 7) == 0


def test_multiply_by_zero():
    assert multiply(999, 0) == 0


def test_divide_returns_decimal():
    assert divide(5, 2) == 2.5


def test_divide_negative_number():
    assert divide(-10, 2) == -5


def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(10, 0)


@pytest.mark.parametrize("value", ["5", None, True])
def test_invalid_numbers_raise_type_error(value):
    with pytest.raises(TypeError, match="Numbers must be int or float"):
        add(value, 2)
