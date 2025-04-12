history = []

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def add_to_history(entry):
    history.append(entry)

def print_history():
    print("\nCalculation History:")
    for h in history:
        print(h)

def undo_last():
    if history:
        removed = history.pop()
        print(f"Undone: {removed}")
    else:
        print("No history to undo")

def main():
    print("Calculator with History and Undo - Add, Subtract, Multiply, Divide")
    op = input("Enter operation (+, -, *, /, undo): ")

    if op == 'undo':
        undo_last()
    elif op in ['+', '-', '*', '/']:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            return

        if op == '+':
            result = add(a, b)
        elif op == '-':
            result = subtract(a, b)
        elif op == '*':
            result = multiply(a, b)
        elif op == '/':
            result = divide(a, b)

        print("Result:", result)
        add_to_history(f"{a} {op} {b} = {result}")
    else:
        print("Invalid operation")
        return

    print_history()

if __name__ == "__main__":
    main()
