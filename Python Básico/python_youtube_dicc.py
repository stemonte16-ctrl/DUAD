my_dict = dict()
my_other_dict = {}

my_other_dict = {
    "Name" : "Steven",
    "Lastname" : "Montenegro",#Aqui la clave(keys) es "Name" y el valor(value) es "steven"
    "Age" : 27
}
my_dict = {
    "Name" : "Steven",
    "Lastname" : "Montenegro",#Aqui la clave(keys) es "Name" y el valor(value) es "steven"
    "Age" : 27,
    "languages" : {"python", "swift", "koltin"}#Aquí hay un diccionario que como clave tiene un str y como valor un set
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Name"])

my_dict["Name"] = "Oscar"
print(my_dict["Name"])

my_dict["Calle"] = "mora"# Aquí sirve para poder meter otro keys y otro value al dict
print(my_dict)

del my_dict["Calle"]#Esto ayuda a eliminar clave y valor juntas
print(my_dict)