"""Exceptions"""
try:
    name = input("Enter your name: ")

    if name.isdigit():
        raise ValueError("The name can not be a number")

    try:
        age = int(input("Enter your age: "))
        print(f"Hello {name}, your age is {age}")
    except ValueError:
        print("invalid number")

except ValueError as e:
    print(e)
