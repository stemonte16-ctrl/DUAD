"""list"""

numbers = input("Enter your list: ")
numb = numbers.split()
numb = [int(n) for n in numb]

all_positive = True

for n in numb:
    if n <= 0:
        all_positive = False
        break

if all_positive:
    print("All are positive")
else:
    print("There is at least one negative number or zero")