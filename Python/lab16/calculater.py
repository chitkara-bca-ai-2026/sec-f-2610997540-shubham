
def format_number(n):
    if n is None:
        return None

    if n == int(n):
        return int(n)

    return n


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


def modulus(a, b):
    if b == 0:
        return None
    return a % b


def power(base, exp=2):
    return base ** exp


def get_number(message):
    n = float(input(message))
    return format_number(n)


def show_menu():
    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (Default: Square)")
    print("7. View Calculation History")
    print("8. Exit")


def main():
    history = []

    print("=" * 40)
    print("    ENTERPRISE UTILITY CALCULATOR")
    print("=" * 40)

    while True:
        show_menu()

        choice = input("Enter your choice (1-8): ")

        if choice == "8":
            print("Calculator closed. Goodbye!")
            break

        elif choice == "7":
            if len(history) == 0:
                print("No calculations performed yet.")
            else:
                print("\nCalculation History:")

                count = 1

                for record in history:
                    print(count, ".", record)
                    count = count + 1

            continue

        elif choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice! Please select from 1 to 8.")
            continue

        try:
            a = get_number("Enter first number: ")

            if choice == "6":
                exponent = input(
                    "Enter exponent (Press Enter for default 2): "
                )

                if exponent == "":
                    result = power(a)
                    expression = str(a) + " ** 2"
                else:
                    exponent = float(exponent)
                    result = power(a, exponent)
                    expression = str(a) + " ** " + str(exponent)

            else:
                b = get_number("Enter second number: ")

                if choice == "1":
                    result = add(a, b)
                    expression = str(a) + " + " + str(b)

                elif choice == "2":
                    result = subtract(a, b)
                    expression = str(a) + " - " + str(b)

                elif choice == "3":
                    result = multiply(a, b)
                    expression = str(a) + " * " + str(b)

                elif choice == "4":
                    if b == 0:
                        print("Error! Cannot divide by zero.")
                        continue

                    result = divide(a, b)
                    expression = str(a) + " / " + str(b)

                elif choice == "5":
                    if b == 0:
                        print("Error! Cannot calculate modulus by zero.")
                        continue

                    result = modulus(a, b)
                    expression = str(a) + " % " + str(b)

            result = format_number(result)

            record = expression + " = " + str(result)

            history.append(record)

            print("[RESULT]", record)

        except ValueError:
            print("Error! Please enter valid numbers.")


if __name__ == "__main__":
    main()
