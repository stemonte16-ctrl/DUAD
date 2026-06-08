with open("nuevo2.0.txt", "r", encoding="utf-8") as file:
    content = file.readlines()
    content = [line.upper() for line in content]
with open("upper.txt", "w", encoding="utf-8") as file:
    file.writelines(content)