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


def modulus(a, b):
    if b == 0:
        return "Cannot use modulus with zero"
    return a % b


while True:
    print("\n----- CALCULATOR -----")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "6":
        print("Calculator closed.")
        break

    if choice in ["1", "2", "3", "4", "5"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            result = add(a, b)
        elif choice == "2":
            result = subtract(a, b)
        elif choice == "3":
            result = multiply(a, b)
        elif choice == "4":
            result = divide(a, b)
        elif choice == "5":
            result = modulus(a, b)

        print("Result:", result)
    else:
        print("Invalid choice. Please choose from 1 to 6.")
