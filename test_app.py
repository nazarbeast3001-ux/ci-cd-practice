"""Юнит-тесты для приложения Calculator"""
import pytest
from app import Calculator

calc = Calculator()


def test_add():
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0
    assert calc.add(2.5, 3.5) == 6.0


def test_subtract():
    assert calc.subtract(10, 4) == 6
    assert calc.subtract(0, 5) == -5
    assert calc.subtract(-5, -3) == -2


def test_multiply():
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(0, 5) == 0


def test_divide():
    assert calc.divide(12, 4) == 3
    assert calc.divide(5, 2) == 2.5
    assert calc.divide(-10, 2) == -5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Division by zero"):
        calc.divide(5, 0)


def test_power():
    assert calc.power(2, 3) == 8
    assert calc.power(5, 0) == 1
    assert calc.power(2, -1) == 0.5


def test_sqrt():
    assert calc.sqrt(16) == 4
    assert calc.sqrt(2) == pytest.approx(1.41421356, rel=1e-6)


def test_sqrt_negative():
    with pytest.raises(ValueError, match="Cannot take sqrt of negative number"):
        calc.sqrt(-5)


@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (2.5, 3.5, 6.0),
    (100, 200, 300),
])
def test_add_parametrized(a, b, expected):
    assert calc.add(a, b) == expected
