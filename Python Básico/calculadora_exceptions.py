"""Exceptions"""

def show_menu(current_number):
    print("\n--- CALCULATOR ---")
    print("Current number:", current_number)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Reset result")
    print("6. Exit")


def get_number():
    while True:
        try:
            return float(input("Enter a number: "))
        except ValueError:
            print("Error: You must enter a valid number.")


def add(current):
    return current + get_number()


def subtract(current):
    return current - get_number()


def multiply(current):
    return current * get_number()


def divide(current):
    num = get_number()
    if num == 0:
        print("Error: Cannot divide by zero.")
        return current
    return current / num


def reset_result():
    return 0



current_number = get_number() 

while True:
    show_menu(current_number)
    option = input("Select an option: ")

    if option == "1":
        current_number = add(current_number)
    elif option == "2":
        current_number = subtract(current_number)
    elif option == "3":
        current_number = multiply(current_number)
    elif option == "4":
        current_number = divide(current_number)
    elif option == "5":
        current_number = reset_result()
        print("Result has been reset.")
    elif option == "6":
        print("Exiting calculator...")
        break
    else:
        print("Error: Invalid option.")