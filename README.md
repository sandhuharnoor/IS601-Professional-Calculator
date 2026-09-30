# IS601 Professional Calculator

A professional command-line calculator application developed in Python for IS601.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Interactive REPL interface
- Calculation history
- Help and exit commands
- Input validation
- Division-by-zero error handling
- Object-oriented design
- Automated testing with pytest
- 100% test coverage
- Continuous Integration with GitHub Actions

## Commands

Run the calculator and use the following commands:

- `add <number1> <number2>`
- `subtract <number1> <number2>`
- `multiply <number1> <number2>`
- `divide <number1> <number2>`
- `history`
- `help`
- `exit`

Example:

`add 10 5`

Output:

`15.0`

## Installation

Clone the repository and enter the project directory.

Create a virtual environment:

`python -m venv .venv`

Activate the virtual environment and install dependencies:

`pip install -r requirements.txt`

## Running the Calculator

Run:

`python -m app.main`

## Testing

Run the test suite with coverage:

`pytest --cov=app --cov-report=term-missing`

The project maintains **100% test coverage**.

## Continuous Integration

GitHub Actions automatically runs the test suite on pushes and pull requests to the main branch. The CI workflow requires 100% test coverage.