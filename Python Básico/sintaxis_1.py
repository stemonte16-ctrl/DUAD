"""age exercises"""

name = input("Enter your name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))

if age >= 65:
    age_group = "Older Adult"
elif age >= 30:
    age_group = "Adult"
elif age >= 18:
    age_group = "Young Adult"
elif age >= 12:
    age_group = "Preteen"
elif age >= 4:
    age_group = "Child"
else:
    age_group = "Baby"

print(f"Hello {name} {last_name} you are {age_group} ")
#no entendi este error porque veo que el codigo funciona
