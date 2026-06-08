"""list"""

numbers = input("Write numbers separated by spaces: ")
list = numbers.split()
list = [int(n) for n in list]
number_to_search = int(input("Which number do you want to search for?:"))
amount = list.count(number_to_search)

print(f"The number {number_to_search} appears {amount} times ")
