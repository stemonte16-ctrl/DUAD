import json

def add_pokemon():

    with open("pokemon.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    name = input("Enter a new Pokemon: ")
    pokemon_type = input("Enter the pokemon type: ")

    while True:
        try:
            level = int(input("Enter the level: "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    while True:
        try:
            weight_kg = float(input("Enter the weight: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    respuesta = input("Is the pokemon shiny? (yes/no): ").lower()

    while respuesta not in ["yes", "no"]:
        respuesta = input("Is the pokemon shiny? (yes/no): ").lower()

    is_shiny = respuesta == "yes"

    held_item = input("Enter held item (leave blank if none): ")

    if held_item == "":
        held_item = None

    skills = []

    for i in range(4):
        skill = input(f"Enter skill {i + 1}: ")
        skills.append(skill)

    stats = {}

    for stat in ["hp", "attack", "defense", "sp_attack", "sp_defense", "speed"]:
        while True:
            try:
                stats[stat] = int(input(f"Enter {stat}: "))
                break
            except ValueError:
                print("Please enter a valid integer.")

    new_pokemon = {
        "name": name,
        "type": pokemon_type,
        "level": level,
        "weight_kg": weight_kg,
        "is_shiny": is_shiny,
        "held_item": held_item,
        "skills": skills,
        "stats": stats
    }

    data.append(new_pokemon)

    with open("pokemon.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print("Pokemon added successfully!")

add_pokemon()