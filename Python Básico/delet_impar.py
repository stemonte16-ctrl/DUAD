"""delete odds"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

my_list = [number for number in my_list if number % 2 == 0]
print(my_list)