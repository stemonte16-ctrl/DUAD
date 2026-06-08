import json

def average():

    with open("pokemon.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    types = {}

    for pokemon in data:
        pokemon_type = pokemon["type"]
        level = pokemon["level"]

        if pokemon_type not in types:
            types[pokemon_type] = {
                "suma": level,
                "cantidad": 1
            }
        else:
            types[pokemon_type]["suma"] += level
            types[pokemon_type]["cantidad"] += 1

    for pokemon_type, datos in types.items():
        promedio = datos["suma"] / datos["cantidad"]
        print(f"Tipo: {pokemon_type} -> Promedio de nivel: {promedio}")

average()