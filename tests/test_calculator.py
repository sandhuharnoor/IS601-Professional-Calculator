import pytest

from app.calculator import Calculator


def test_calculator_starts_empty():
    calculator = Calculator()
    assert calculator.history == []


def test_add_calculation():
    calculator = Calculator()
    result = calculator.calculate("add", 10, 5)

    assert result == 15
    assert len(calculator.history) == 1


def test_subtract_calculation():
    calculator = Calculator()
    assert calculator.calculate("subtract", 10, 5) == 5


def test_multiply_calculation():
    calculator = Calculator()
    assert calculator.calculate("multiply", 10, 5) == 50


def test_divide_calculation():
    calculator = Calculator()
    assert calculator.calculate("divide", 10, 5) == 2


def test_divide_by_zero():
    calculator = Calculator()

    with pytest.raises(ZeroDivisionError):
        calculator.calculate("divide", 10, 0)


def test_invalid_operation():
    calculator = Calculator()

    with pytest.raises(ValueError):
        calculator.calculate("invalid", 10, 5)


def test_history():
    calculator = Calculator()

    calculator.calculate("add", 10, 5)
    calculator.calculate("subtract", 10, 5)

    assert len(calculator.history) == 2


def test_clear_history():
    calculator = Calculator()

    calculator.calculate("add", 10, 5)
    calculator.clear_history()

    assert calculator.history == []


def test_help():
    calculator = Calculator()
    help_text = calculator.help()

    assert "add" in help_text
    assert "subtract" in help_text
    assert "multiply" in help_text
    assert "divide" in help_text
    assert "history" in help_text
    assert "exit" in help_text
def test_calculator_history_property():
    calculator = Calculator()
    calculator.calculate("add", 10, 5)
    assert calculator.history[0] is not None