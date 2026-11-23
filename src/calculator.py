"""Small mathematical helpers used in the CI lab."""


def add(left: float, right: float) -> float:
    """Return the sum of two numbers."""
    validate_numbers(left, right)
    return left + right


def subtract(left: float, right: float) -> float:
    """Subtract right from left."""
    validate_numbers(left, right)
    return left - right


def multiply(left: float, right: float) -> float:
    """Multiply two numbers."""
    validate_numbers(left, right)
    return left * right


def divide(left: float, right: float) -> float:
    """Divide left by right."""
    validate_numbers(left, right)
    if right == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return left / right


def validate_numbers(*values: float) -> None:
    """Reject values that are not real numbers."""
    for value in values:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("Numbers must be int or float values")
