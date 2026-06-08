"""multiplication table"""

number = int(input("Enter the number: "))
counter_multi = 0
result = 0

while counter_multi <= 12:
    result = number * counter_multi
    print(number, "*",  counter_multi, "=",  result)
    counter_multi += 1
