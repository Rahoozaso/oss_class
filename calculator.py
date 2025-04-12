def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def main():
    #Main branch modification forconflict test
    print("Simple Calculator - Add and Subtract")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation (+ or -): ")

    if op == '+':
        print("Result:", add(a, b))
    elif op == '-':
        print("Result:", subtract(a, b))
    else:
        print("Invalid operation")

if __name__ == "__main__":
    main()
