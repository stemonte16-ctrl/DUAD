"""diccionarios"""

employee = {
    "name" : "Steven",
    "email" : "stevemonte@gmail.com",
    "acces_level" : 5,
    "age" : 27
}

delete_list_keys = ["acces_level", "age"]

for clave in delete_list_keys:
    employee.pop(clave, None)

print(employee)
