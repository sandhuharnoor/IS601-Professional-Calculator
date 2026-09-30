from app.calculator import Calculator


def display_history(calculator):
    """Display all calculations performed during this session."""
    history = calculator.get_history()

    if not history:
        print("No calculations in history.")
        return

    print("\nCalculation History:")
    for index, calculation in enumerate(history, start=1):
        print(f"{index}. {calculation}")


def process_calculation(calculator, command, parts):
    """Validate input and perform a calculation."""
    # LBYL: check the number of arguments before using them.
    if len(parts) != 3:
        print(f"Usage: {command} <number1> <number2>")
        return

    # EAFP: attempt conversion and handle bad input if it occurs.
    try:
        first_number = float(parts[1])
        second_number = float(parts[2])
        result = calculator.calculate(
            command,
            first_number,
            second_number
        )
        print(f"Result: {result}")

    except ValueError:
        print("Error: Please enter valid numbers.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")


def repl():
    """Run the calculator Read-Eval-Print Loop."""
    calculator = Calculator()

    print("Professional Calculator")
    print("Type 'help' to see available commands.")

    while True:
        try:
            user_input = input("\n>>> ").strip()

            if not user_input:
                print("Please enter a command.")
                continue

            parts = user_input.split()
            command = parts[0].lower()

            if command == "exit":
                print("Goodbye!")
                break

            if command == "help":
                print(calculator.help())
                continue

            if command == "history":
                display_history(calculator)
                continue

            if command in {"add", "subtract", "multiply", "divide"}:
                process_calculation(calculator, command, parts)
                continue

            print("Unknown command. Type 'help' for available commands.")

        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    repl()