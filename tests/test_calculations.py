import pytest

from app.calculation import Calculation, CalculationFactory
from app.operation import Addition, Subtraction, Multiplication, Division


def test_calculation():
    calculation = Calculation(10, 5, Addition)
    assert calculation.perform() == 15


@pytest.mark.parametrize(
    "operation_name,operation_class",
    [
        ("add", Addition),
        ("subtract", Subtraction),
        ("multiply", Multiplication),
        ("divide", Division),
    ],
)
def test_factory_operations(operation_name, operation_class):
    calculation = CalculationFactory.create(operation_name, 10, 5)
    assert calculation.operation == operation_class


def test_factory_invalid_operation():
    with pytest.raises(ValueError):
        CalculationFactory.create("invalid", 10, 5)


def test_calculation_string():
    calculation = Calculation(10, 5, Addition)
    assert "10" in str(calculation)
    assert "5" in str(calculation)