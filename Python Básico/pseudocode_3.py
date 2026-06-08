"""number"""

number = int(input("Enter the number:"))
counter = 1
sum = 0

while counter <= number:
    sum = sum + counter
    counter = counter + 1

print(sum)
