"""input 10"""

list = []
larger_number = None

for numb in range(10):
    number = int(input("Enter the number: "))
    list.append(number)
    
    if larger_number is None or number > larger_number:
        larger_number = number

print(f"{list}. The larger number was {larger_number}. ")
