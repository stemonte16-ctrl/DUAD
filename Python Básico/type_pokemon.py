import json

def type_pokemon():
    
    with open("pokemon.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        
    user = input("Enter the type of Pokémon you want to search for: ").lower()
    
    print(f"The {user} pokemon are: ")
    for pokemon in data:
        if pokemon["type"].lower() == user:
            print(pokemon["name"])


type_pokemon()