with open("nuevo.txt", "r", encoding="utf-8") as file:
    text = file.read()
    words = text.split()
    word_count = len(words)
    print(f"El número de palabras en el archivo es: {word_count}")