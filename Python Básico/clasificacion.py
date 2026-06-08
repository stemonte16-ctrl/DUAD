import csv

def read_video_games(file_path):
    
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        calificacion = input("Ingrese clasificacion: ")
        for row in reader:
            if row[3] == calificacion:
                print(row)
read_video_games("video games.csv")