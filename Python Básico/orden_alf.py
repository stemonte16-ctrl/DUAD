"""alphabetical order"""

# Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabéticamente.
# Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
# “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”


def to_arrange_words(text):
    
    list_1 = text.split("-")
    
    list_1 = [word.strip() for word in list_1]
    
    list_1.sort()
    
    return "-".join(list_1)

print(to_arrange_words("python-funcion-monitor-variable-computador"))