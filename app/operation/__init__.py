class Operation:
    """Base class for calculator operations."""

    @staticmethod
    def execute(a, b):
        raise NotImplementedError("Operation must implement execute().")


class Addition(Operation):
    @staticmethod
    def execute(a, b):
        return a + b


class Subtraction(Operation):
    @staticmethod
    def execute(a, b):
        return a - b


class Multiplication(Operation):
    @staticmethod
    def execute(a, b):
        return a * b


class Division(Operation):
    @staticmethod
    def execute(a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b