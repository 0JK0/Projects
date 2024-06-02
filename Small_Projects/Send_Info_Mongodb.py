import json
import pymongo
import time

# En my pc es 27017 cambia este numero si es necesario
# Las colecciones son Case sensitive
# Se salva tambien en JSON ademas de mandarlo a Mongodb directamente, lo deje asi para probar


client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client["Colegio"]


#Yeah yeah i know i alwasy use this but it took me an annoying while to figure out and i dont want to re do that
def display_options(title,options):
    print("\n")
    print("+-----------------------------------+")
    print(f"|          {title}")
    print("+-----------------------------------+")
    # For option in options do. The "i" is used because it counts up, enumerate enumerates the list starting from the number given (so it starts counting from 1 instead of 0).
    for i, option in enumerate(options, 1): 
        print(f"|  {i}. {option}") # if you ut the {} it will print a variable like text and again the f makes the string more fancy
    print("+-----------------------------------+")

def create_database():
    client = pymongo.MongoClient('mongodb://localhost:27017/')

    existing_database = client.list_database_names()

    new_database_name = input("Enter the name for the new DataBase: ")
    collection_name = input("Enter the name for the 1st collection: ")

    global db

    db = client[new_database_name]
    
    try:
        db.create_collection(collection_name)
        print("Database and Collection created successfully!")
    except Exception as e:
        print("Error: ", e)


def profesores_tabla():
    profesores_collection = db['Profesores']
    while True:
        profesores_list = []
    
        nombre = input("Ingresa el nombre del profesor: ")
        edad = input("Ingresa la edad del profesor: ")
        genero = input("Ingresa el genero: ")
        fecha_nacimiento = input("Ingresa la fecha de nacimiento: ")
        titulo = input("Ingresa el titulo del profesor: ")
        materia = input("Ingresa la materia del profesor: ")

        data_fill = {
            "NOMBRE": nombre,
            "EDAD": edad,
            "GÉNERO": genero,
            "FECHA_NACIMIENTO": fecha_nacimiento,
            "TITULO": titulo,
            "MATERIA": materia}
    
        profesores_list.append(data_fill) 
 

        with open("insert_profesores.json", "w") as jf:
            json.dump(profesores_list, jf)
            jf.write('\n') 

        profesores_collection.insert_many(profesores_list)

        continuar = input("Continuar ingresando profesores? (si/no): ").lower()
        if continuar!= 'si':
             break
        
       

def Materias_tabla():
    materias_list = [] 
    materias_collection = db['Materias']
    
    while True:
        nombre = input("Ingresa el nombre de la materia: ")
        horas = input("Ingresa la cantidad de horas de la materia: ")
        grado = input("Ingresa la clase o grado: ")

        data_fill = {
            "NOMBRE_MATERIA": nombre,
            "HORAS": horas,
            "GRADO": grado
        }

        materias_list.append(data_fill)  
        
       
        continuar = input("Continuar ingresando materias? (si/no): ").lower()
        if continuar!= 'si':
            break

    with open("insert_materias.json", "w") as jf:
        json.dump(materias_list, jf)
    
    materias_collection.insert_many(materias_list)
        
        
def calificaciones_tabla():
    calificaciones_list = [] 
    calificaciones_collection = db['Calificaciones']
    
    while True:
        nombre_estudiante = input("Ingresa el nombre del estudiante: ")
        grado = input("Ingresa el grado o año escolar del estudiante: ")
        profesor = input("Ingresa el nombre del profesor del estudiante: ")
        nota1 = input("Ingresa la primera nota: ")
        nota2 = input("Ingresa la segunda nota: ")
        nota3 = input("Ingresa la tercera nota: ")
        definitiva = input("Ingresa la nota definitiva: ")

        data_fill = {
            "NOMBRE_ESTUDIANTE": nombre_estudiante,
            "GRADO": grado,
            "PROFESOR": profesor,
            "NOTA1": nota1,
            "NOTA2": nota2,
            "NOTA3": nota3,
            "DEFINITIVA": definitiva
        }

        calificaciones_list.append(data_fill)  
        
       
        continuar = input("Continuar ingresando calificaciones? (si/no): ").lower()
        if continuar!= 'si':
            break

    with open("insert_calificaciones.json", "w") as jf:
        json.dump(calificaciones_list, jf)

    calificaciones_collection.insert_many(calificaciones_list)
        
def main():
    main_menu = ["Make New DataBase             | ","Enter new info into existing  |"]
    display_options("MongoDB Connection       |",main_menu)

    start = input("--> ")

    if start == "1":
        create_database()
        print(client.list_database_names())
    elif start == "2":
        tables = ["Profesores","Materias","Calificaciones"]

        display_options("Choose Table",tables)

        uses = input("--> ")

        if uses == "1":
            profesores_tabla()
        elif uses == "2":
            Materias_tabla()
        elif uses == "3":
            calificaciones_tabla()

if __name__ == "__main__":
    main()