nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))
sexo = input("Ingrese su sexo(hombre/mujer): ")
objetivo = input("¿Cuál es tu objetivo? (volumen/definicion/mantenimiento): ")
actividad = input("Nivel de actividad (sedentario/ligero/moderado/intenso): ")

if sexo == "hombre":
    bmr = 10 * peso + 6.25 * altura - 5 * edad +5
else:
    bmr = 10 * peso + 6.25 * altura - 5 * edad - 161

if objetivo == "volumen":
    calorias = bmr + 300
    
elif objetivo == "definicion":
    calorias = bmr - 300

else:
    calorias = bmr

if actividad == "sedentario":
    tdee = bmr * 1.2
elif actividad == "ligero":
    tdee = bmr * 1.375
elif actividad == "moderado":
    tdee = bmr * 1.55
else:
    tdee = bmr * 1.725


print("\n---DATOS DEL USUARIO---")
print(f"Nombre : {nombre}")
print(f"Edad : {edad}")
print(f"Peso : {peso}")
print(f"Altura : {altura}")
print(f"Total de calorias quemadas en reposo : {bmr:.2f}")
print(f"Tus calorias a ingerir en un dia son: {calorias:.2f}")
print(f"Gasto energetico total: {tdee}")
