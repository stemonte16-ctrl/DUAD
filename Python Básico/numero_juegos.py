import csv

def read_video_games(file_path):
    
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        genres = {}
        for row in reader:
            if row[1] in genres:
                genres[row[1]] += 1
            else:
                genres[row[1]] = 1
        print("Generos encontrados:")
        for gen,amount in genres.items():
            print(f"{gen} : {amount}")
read_video_games("video games.csv")