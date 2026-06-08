import csv

import csv


def calcular_promedio():

    with open("personas.csv", "r", encoding="utf-8") as file:
        lector = csv.DictReader(file)

        total_edad = 0
        total_personas = 0

        for fila in lector:
            total_edad += int(fila["Edad"])
            total_personas += 1

        promedio_edad = total_edad / total_personas

        print(f"Promedio de edades: {promedio_edad}")


def encontrar_mayor():

    with open("personas.csv", "r", encoding="utf-8") as file:
        lector = csv.DictReader(file)

        mayor_edad = 0
        nombre_mayor_edad = ""

        for fila in lector:

            edad = int(fila["Edad"])

            if edad > mayor_edad:
                mayor_edad = edad
                nombre_mayor_edad = fila["Nombre"]

        print(f"Mayor edad: {mayor_edad} ({nombre_mayor_edad})")

def encontrar_menor():
    
    with open("personas.csv", "r", encoding="utf-8") as file:
        lector = csv.DictReader(file)
        menor_edad = float('inf')
        nombre_menor_edad = ""
        
        for fila in lector:
            edad = int(fila["Edad"])
            
            if edad < menor_edad:
                menor_edad = edad
                nombre_menor_edad = fila["Nombre"]
                
        print(f"Menor edad: {menor_edad} ({nombre_menor_edad})")

def mayores_de_20():
    
    with open("personas.csv", "r", encoding="utf-8") as file:
        lector = csv.DictReader(file)
        
        for fila in lector:
            edad = int(fila["Edad"])
            
            if edad > 20:
                print(fila['Nombre'])

calcular_promedio()
encontrar_mayor()
encontrar_menor()
mayores_de_20()