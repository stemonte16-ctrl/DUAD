def operar(a, b):
    try:
        return a + b
    except TypeError:
        return "NO es posible sumar un texo con un numero"
    except:
        return "Error"


print(operar("sa", 2))
print(operar(12, 3))