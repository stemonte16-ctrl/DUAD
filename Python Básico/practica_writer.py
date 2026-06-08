import csv

def save_video_games():
    with open("video games.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre","Genero","Desarrollador","Clasificacion"])
        
        for i in range(4):
            
            name = input("Ingrese el nombre del video juego: ")
            gender = input("Ingrese el genero del video juego: ")
            developer = input("Ingrese el desarrollador del video juego: ")
            classification = input("Ingrese la clasificación del video juego: ")
            
            writer.writerow([name, gender, developer, classification])

save_video_games()