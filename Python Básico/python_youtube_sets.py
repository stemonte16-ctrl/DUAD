my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))#inicialmente sale como un diccionario

my_other_set = {"steven", "monte", 34}
print(type(my_other_set))

print(len(my_other_set))

#print(my_other_set[2]) No se puede acceder a los elementos

my_other_set.add("tut")
print(my_other_set) # Un set no es una estructura ordenada
# Un set no admite  elementos repetidos

print("steven" in my_other_set)# Podemos realizar busquedas, en este dice que es True porque si esta en el set
print("stevennnnnnnn" in my_other_set)# Aquí dice False porque no esta

my_other_set.remove("tut")# Tambien se puede eliminar elementos
print(my_other_set)

my_other_set.clear()# Elimina todo lo que hay en el set
print(len(my_other_set))

my_set = {"python", "java", "linux"}
my_el_set = {2, 3, 4}
my_new_set = my_set.union(my_el_set)# Aquí se uniria dos sets
print(my_new_set)

print(my_set.difference(my_el_set))