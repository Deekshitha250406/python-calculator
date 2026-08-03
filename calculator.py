def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


def main():
    print("=" * 40)
    print("      PYTHON CALCULATOR")
    print("=" * 40)

    print("\nChoose an operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "5":
        print("\nThank you for using the calculator!")
        return

    if choice not in ["1", "2", "3", "4"]:
        print("\nInvalid choice! Please select a number between 1 and 5.")
        return

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("\nResult =", add(num1, num2))

    elif choice == "2":
        print("\nResult =", subtract(num1, num2))

    elif choice == "3":
        print("\nResult =", multiply(num1, num2))

    elif choice == "4":
        print("\nResult =", divide(num1, num2))


if __name__ == "__main__":
    main()