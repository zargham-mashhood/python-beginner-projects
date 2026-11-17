"""Simple calculator (command line).

Asks for two numbers and an operation (+, -, *, /) and prints the result.
Division by zero is handled with a friendly message instead of crashing.

Run:  python3 calculator.py
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero."
    return a / b


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def read_number(prompt):
    """Keep asking until the user types a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That is not a number — please try again.")


def main():
    print("--- Simple Calculator ---")
    print("Operations: +  -  *  /")

    num1 = read_number("First number: ")
    num2 = read_number("Second number: ")

    op = input("Operation (+, -, *, /): ").strip()
    if op not in OPERATIONS:
        print("Unknown operation. Please use +, -, * or /.")
        return

    result = OPERATIONS[op](num1, num2)
    print(f"Result: {num1} {op} {num2} = {result}")


if __name__ == "__main__":
    main()
