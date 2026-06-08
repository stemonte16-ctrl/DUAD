with open("nuevo.txt", "r", encoding="utf-8") as file:
    content = file.readlines()
    list_1 = [linea.strip() for linea in content]
    list_1 = " ".join(list_1)
with open("nuevo_unido.txt", "w", encoding="utf-8") as file:
    file.write(list_1)