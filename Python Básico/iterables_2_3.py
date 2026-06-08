"""list"""

numbers = input("Enter your list: ")

nums = numbers.split()  # separa por espacios

new_list = []

for n in nums:
    new_list.append(int(n))

smallest = new_list[0]

for n in new_list:
    if n < smallest:
        smallest = n

print("The smallest number is:", smallest)