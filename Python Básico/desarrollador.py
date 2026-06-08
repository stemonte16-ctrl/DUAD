import csv

def read_video_games(file_path):
    
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        developer = input("Ingrese l nombre del desarrollador: ")
        print(f"Videojuegos desarrollados por {developer} son : ")
        for row in reader:
            if row[2] == developer:
                print(row)

read_video_games("video games.csv")