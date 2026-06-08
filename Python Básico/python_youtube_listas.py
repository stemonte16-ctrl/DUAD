## materia y practica de listas##

my_list = list()#Esto es otra forma de poner las listas
my_other_list = [] # Esta es la que yo he estudiado mas

print(len(my_list))#puse un len que es una operacion que esta dentro del sistema, si le doy ejecutar da 0 porque es una lista vacía
###Una lista es una caja donde yo añado elementos cada uno en una posicion el primer elemento que entra tiene posicion 0
#El segundo 1 y así sucesivamente
my_list = [35, 24, 62, 52, 30, 30,17]

print(my_list)#El len sirve para saber cuantos elementos hay
print(len(my_list))#Una lista es una forma de agrupar datos

my_other_list = [27, 1.73, "steven", "montenegro"]#no da error a la hora de ejecutar porque se pueden convinar datos

print(type(my_other_list))

print(my_other_list[0])# esto es para ver el indice #27
print(my_other_list[1])#1.73
print(my_other_list[2])#"steven"
print(my_other_list[3])#"montenegro" 
print(my_other_list.count(27))#El COUNT sirve para ver cuantas veces sale un valor

print(my_other_list + my_list)##Hciendo esto hemos logrado CONCATENAR las listas osea unirlas

my_other_list.append("traca traca")#El append sir ve para AGREGAR al FINAL el elemento que quieres poner en la lista
print(my_other_list)

my_other_list.insert(2,"coco")#Hay que insertar el indice que es la posición luego del indice poner el int o el str
print(my_other_list)

my_other_list.remove("coco")#Solo elimina el primer elemento 
print(my_other_list)

#my_other_list.clear()   #Sirve para vaciar completamente una lista
#print(my_other_list)

new_list = my_other_list.copy()#Copia la lista, hay que hacer otra variable para hacer la nueva copia y detro de la variable 
print(new_list)# la lista anterior con .copy() y en el print se pone la new list

my_other_list.extend(my_list)#agrega los elementos de las dos listas y la convierte en una sola lista
print(my_other_list)

position = my_other_list.index("steven")#Sirve para saber la posicion del elemento en la lista, se puede mostrar directamente 
print(f"Este en la posicion {position}")#Así print(my_other_list.index(20)) pero es mas oredenado con una variable

my_other_list.insert(2, "fufi")#Sirve para insertar un elemento en una posición específica yo puse "steven" en el indice 2
print(my_other_list)

#my_pop_element = my_other_list.pop(2) # si lo guardo el que elimine en una variable lo puedo volver a obtener
my_other_list.pop(0)#pop() se usa para eliminar un elemento y al mismo tiempo obtenerlo.
print(my_other_list) #Elimina el ultimo valor por defecto.

my_other_list.reverse()
print(my_other_list)# reverse() es para invertir la lista 

otra_listilla = ["hola", "ana", "benecia"]

otra_listilla.sort()# sirve para acomodar la lista alfabeticamente
print(otra_listilla)

texto = " , ".join(otra_listilla)
print(texto)