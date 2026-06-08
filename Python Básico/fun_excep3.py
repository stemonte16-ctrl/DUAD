"""def and exception"""

def sum_total(my_list):
    sum = 0

    for element in my_list:
        try:
            number = float(element)
            sum += number
            print(f"{number} added correctly")
        except ValueError:
            print(f"Invalid element: {element}")

    print(f"Total of the added: {sum}")


my_list = ["10", "juju", "5.5", "3"]

sum_total(my_list)
