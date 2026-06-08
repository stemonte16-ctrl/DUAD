"""scope"""

# Intente acceder a una variable definida dentro de una función desde afuera.
number_outside = 4
def my_funcion():
    print("inside:", number_outside)


my_funcion()

print("outside:", number_outside)# Da error porque no esta definida


#Intente acceder a una variable global desde una función y cambiar su valor.
number = 9

def my_new_function():
    global number
    number = number + 2
    print(number)

my_new_function()
