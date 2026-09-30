import runpy
from unittest.mock import patch

from app.main import display_history, process_calculation, repl
from app.calculator import Calculator


def test_display_history_empty(capsys):
    calculator = Calculator()

    display_history(calculator)

    output = capsys.readouterr().out
    assert "No calculations in history." in output


def test_display_history_with_calculation(capsys):
    calculator = Calculator()
    calculator.calculate("add", 10, 5)

    display_history(calculator)

    output = capsys.readouterr().out
    assert "Calculation History:" in output
    assert "15" in output


def test_process_calculation_add(capsys):
    calculator = Calculator()

    process_calculation(calculator, "add", ["add", "10", "5"])

    output = capsys.readouterr().out
    assert "15" in output


def test_process_calculation_subtract(capsys):
    calculator = Calculator()

    process_calculation(
        calculator,
        "subtract",
        ["subtract", "10", "5"]
    )

    output = capsys.readouterr().out
    assert "5" in output


def test_process_calculation_multiply(capsys):
    calculator = Calculator()

    process_calculation(
        calculator,
        "multiply",
        ["multiply", "10", "5"]
    )

    output = capsys.readouterr().out
    assert "50" in output


def test_process_calculation_divide(capsys):
    calculator = Calculator()

    process_calculation(
        calculator,
        "divide",
        ["divide", "10", "5"]
    )

    output = capsys.readouterr().out
    assert "2" in output


def test_process_calculation_missing_arguments(capsys):
    calculator = Calculator()

    process_calculation(
        calculator,
        "add",
        ["add", "5"]
    )

    output = capsys.readouterr().out
    assert "Usage:" in output


def test_process_calculation_invalid_numbers(capsys):
    calculator = Calculator()

    process_calculation(
        calculator,
        "add",
        ["add", "hello", "5"]
    )

    output = capsys.readouterr().out
    assert "valid numbers" in output


def test_process_calculation_divide_by_zero(capsys):
    calculator = Calculator()

    process_calculation(
        calculator,
        "divide",
        ["divide", "10", "0"]
    )

    output = capsys.readouterr().out
    assert "divide by zero" in output.lower()


@patch(
    "builtins.input",
    side_effect=[
        "",
        "help",
        "add 10 5",
        "subtract 10 5",
        "multiply 10 5",
        "divide 10 5",
        "history",
        "something",
        "exit",
    ],
)
def test_repl_commands(mock_input, capsys):
    repl()

    output = capsys.readouterr().out

    assert "Professional Calculator" in output
    assert "15" in output
    assert "Calculation History:" in output
    assert "Unknown command" in output
    assert "Goodbye!" in output


@patch("builtins.input", side_effect=EOFError)
def test_repl_eof(mock_input, capsys):
    repl()

    output = capsys.readouterr().out
    assert "Goodbye!" in output


@patch("builtins.input", side_effect=KeyboardInterrupt)
def test_repl_keyboard_interrupt(mock_input, capsys):
    repl()

    output = capsys.readouterr().out
    assert "Goodbye!" in output


def test_main_runs_as_script():
    with patch("builtins.input", side_effect=["exit"]):
        runpy.run_module("app.main", run_name="__main__")