"""larger number"""

number_1 = int(input("Enter number 1: "))
number_2 = int(input("Enter number 2: "))
number_3 = int(input("Enter number 3: "))

if number_1 > number_2 and number_1 > number_3:
    print("The larger is the number 1")
elif number_2 > number_3:
    print("The larger is the number 2")
else:
    print("The larger is the number 3")

print("Thank you for playing")
