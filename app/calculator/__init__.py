from app.calculation import CalculationFactory


class Calculator:
    """Calculator that performs operations and stores calculation history."""

    def __init__(self):
        self.history = []

    def calculate(self, operation, a, b):
        """Create and perform a calculation."""
        calculation = CalculationFactory.create(operation, a, b)
        result = calculation.perform()
        self.history.append(calculation)
        return result

    def get_history(self):
        """Return calculation history."""
        return self.history

    def clear_history(self):
        """Clear all calculations from history."""
        self.history.clear()

    @staticmethod
    def help():
        """Return the available calculator commands."""
        return (
            "Available commands:\n"
            "  add <number1> <number2>\n"
            "  subtract <number1> <number2>\n"
            "  multiply <number1> <number2>\n"
            "  divide <number1> <number2>\n"
            "  history\n"
            "  help\n"
            "  exit"
        )