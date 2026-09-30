import pytest

from app.operation import (
    Addition,
    Subtraction,
    Multiplication,
    Division,
)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10, 5, 15),
        (-5, 5, 0),
        (2.5, 2.5, 5),
    ],
)
def test_addition(a, b, expected):
    assert Addition.execute(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10, 5, 5),
        (5, 10, -5),
        (2.5, 1.5, 1),
    ],
)
def test_subtraction(a, b, expected):
    assert Subtraction.execute(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10, 5, 50),
        (-2, 5, -10),
        (2.5, 2, 5),
    ],
)
def test_multiplication(a, b, expected):
    assert Multiplication.execute(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10, 5, 2),
        (5, 2, 2.5),
        (-10, 5, -2),
    ],
)
def test_division(a, b, expected):
    assert Division.execute(a, b) == expected


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        Division.execute(10, 0)
def test_base_operation_execute():
    from app.operation import Operation

    with pytest.raises(NotImplementedError):
        Operation.execute(10, 5)