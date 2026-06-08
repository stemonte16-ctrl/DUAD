# CAMBIO DE TEXTO
name = "hola_mundo"
texto = " Porque de tal manera amó Dios al mundo que dio a su hijo Jesús....."
title = "Hola Mundo"
my_list = ["hola", "Mundo"]
print(texto.lower()) # Convierte todo en minúscula

print(texto.upper()) # Convierte todo en mayúscula

print(texto.capitalize()) # Deja solo la primera letra en mayúscula , las demás en minúsculas

print(texto.title()) # Convierte a cada palabra la primera letra en mayúscula

print(texto.swapcase()) # Cambia las mayúsculas por las minúsculas

print(texto.casefold()) # Convierte todo en minúscula igual que (.lower)

print(len(texto)) # SIrve para contar cuantos elementos hay en un str

print(texto.center(72, "=")) # Sirve para formatear texto

print(texto.count("a")) # Cuenta cuántas veces aparece algo dentro de un string

print(texto.encode()) # Son datos en formato que la computadora entiende directamente

print(texto.endswith("Jesús")) # Devuelve True si el string termina con esa subcadena(es alguna parte del texto )

print(texto.find("Jesús")) # Busca una subcadena dentro del string y devuelve su posición (índice)

print(texto.format()) #Inserta valores dentro de un string, no se bien como usarlo

# VERIFICACIÓN (TRUE/ FALSE)

print(texto.isalnum()) # Devuelve True si el string contiene solo letras y número, Devuelve False si hay cualquier otro carácter

print(texto.isalpha()) # Devuelve True si el string contiene solo letras, Devuelve False si hay cualquier otra cosa

print(texto.isascii()) # Devuelve True si todos los caracteres del string son ASCII, Devuelve False si hay caracteres fuera de ASCII
# letras inglesas → a-z, A-Z, números → 0-9, símbolos básicos → ! @ # $ %, espacio(Esto es ASCII)
# NO incluye: ñ, á, emojis 😄, caracteres especiales de otros idiomas

print(name.isdecimal())

print(name.isdigit()) # Devuelve True si el string contiene solo dígitos (números), Devuelve False si hay cualquier otro carácter

print(name.isidentifier()) # Devuelve True si el string es un nombre válido de variable en Python, Devuelve False si no lo es

print(texto.islower()) # Devuelve True si todas las letras del string están en minúscula, Devuelve False si hay alguna letra en mayúscula

print(texto.isnumeric()) # Devuelve True si el string contiene solo caracteres numéricos, Devuelve False si hay cualquier otro carácter

print(texto.isprintable()) # Devuelve True si todos los caracteres se pueden mostrar (imprimir), Devuelve False si hay caracteres “invisibles” o de control

print(texto.isspace()) # Devuelve True si el string contiene solo espacios en blanco, Devuelve False si hay cualquier otro carácter

print(title.istitle()) # Devuelve True si el string está en formato título, Devuelve False si no lo está

print(texto.isupper()) # Devuelve True si todas las letras están en MAYÚSCULA, Devuelve False si hay alguna letra en minúscula

# BUSQUEDA

print(texto.find("z")) #Busca una subcadena dentro de un string, Devuelve la posición (índice) donde empieza, Si no la encuentra → devuelve -1

print(texto.index("de"))   # posición o error

print(texto.count("d"))      # cuántas veces aparece

print(texto.startswith("P")) # letra con que empieza

print(texto.endswith("s")) # Letra con que termina

# MODIFICACIÓN

print(texto.replace("Jesús", "Cristo")) # Remplaza la palabra 

print(texto.strip()) # Elimina los espacios (u otros caracteres) al inicio y al final del string

print(texto.lstrip()) # Elimina los espacios (u otros caracteres) solo del lado izquierdo (inicio) del string

print(texto.rstrip()) # Elimina los espacios (u otros caracteres) solo del lado derecho (inicio) del string

print(texto.split()) # Divide un string en una lista

print(" ".join(my_list)) # Une elementos de una lista (u otro iterable) en un solo string

print(texto[::-1]) # asi se vuelve al revés todo el texto