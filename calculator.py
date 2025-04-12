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

def main():
    print("Calculator with History - Add, Subtract, Multiply, Divide")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")

    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = subtract(a, b)
    elif op == '*':
        result = multiply(a, b)
    elif op == '/':
        result = divide(a, b)
    else:
        print("Invalid operation")
        return

    print("Result:", result)
    add_to_history(f"{a} {op} {b} = {result}")
    print_history()

if __name__ == "__main__":
    main()
