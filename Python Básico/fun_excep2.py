"""def and exception"""

def become_to_int(my_list):
    
    for element in my_list:
        try:
            number = int(element)
            print(f"{element} become to {number} ")
        except ValueError:
            print(f"Could not convert the item: {element}")
my_list = ["4", "hola", "10", "5.2"]
become_to_int(my_list)