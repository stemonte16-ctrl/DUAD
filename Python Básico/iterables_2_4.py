"""list"""

numbers = input("Enter the list: ")
nums = numbers.split()
nums = [int(n) for n in nums ]
total = 0

for n in nums:
    total += n

average = total / len(nums)

new_list = []

for n in nums:
    if n > average:
        new_list.append(n)

print(average)
print(new_list)