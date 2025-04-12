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
    print("Calculation History:")
    for h in history:
        print(h)

def undo_last():
    if history:
        removed = history.pop()
        print(f"Undone: {removed}")
    else:
        print("No history to undo")

def main():
    print("Calculator with History and Undo")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /, undo): ")

    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = subtract(a, b)
    elif op == '*':
        result = multiply(a, b)
    elif op == '/':
        result = divide(a, b)
    elif op == 'undo':
        undo_last()
        return
    else:
        print("Invalid operation")
        return

    print("Result:", result)
    add_to_history(f"{a} {op} {b} = {result}")
    print_history()

if __name__ == "__main__":
    main()

