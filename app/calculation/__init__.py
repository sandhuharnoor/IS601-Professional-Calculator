from app.operation import Addition, Subtraction, Multiplication, Division


class Calculation:
    """Represents a single calculation."""

    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def perform(self):
        """Perform and return the calculation."""
        return self.operation.execute(self.a, self.b)

    def __str__(self):
        return (
            f"{self.a} {self.operation.__name__} "
            f"{self.b} = {self.perform()}"
        )


class CalculationFactory:
    """Creates calculation objects based on an operation name."""

    operations = {
        "add": Addition,
        "subtract": Subtraction,
        "multiply": Multiplication,
        "divide": Division,
    }

    @classmethod
    def create(cls, operation_name, a, b):
        operation_name = operation_name.lower()

        # LBYL: verify the operation exists before accessing it.
        if operation_name not in cls.operations:
            raise ValueError(f"Unknown operation: {operation_name}")

        operation = cls.operations[operation_name]
        return Calculation(a, b, operation)