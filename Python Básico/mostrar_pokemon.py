import json 

def show_info_pokemon():
    
    with open("pokemon.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    
    for pokemon in data:
        print(f"Name: {pokemon["name"]}, Type: {pokemon["type"]} , Level: {pokemon["level"]}")
        

show_info_pokemon()