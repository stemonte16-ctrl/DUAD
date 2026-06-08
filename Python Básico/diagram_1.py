"""secret number"""

secret_number = 3
number = int(input("Enter the number: "))

while number != secret_number:
    number = int(input("Enter the number again: "))

print("You guessed")
