import json

def show_statistics():
    
    with open("pokemon.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    
    for pokemon in data:
        print(f"Name: {pokemon["name"]}")
        print(f"Attack: {pokemon["stats"]["attack"]}")
        print(f"Defense: {pokemon["stats"]["defense"]}")
        print(f"Speed: {pokemon["stats"]["speed"]}")
        print()

show_statistics()