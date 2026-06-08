"""secret number"""

user = int(input("Enter a number: "))
import random
secret_number = random.randint(1, 10)
guess = 0

while guess != secret_number:
    print("Try again")
    guess = int(input("Enter a number again: "))

print("you did it")
