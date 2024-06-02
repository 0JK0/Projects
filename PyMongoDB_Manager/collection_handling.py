import json
import pymongo


class collections:

    def __init__(self,DataBase):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.DataBase = DataBase


    def profesores_tabla(self):

        
        db = self.client[f"{self.DataBase}"]

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
            
        

    def Materias_tabla(self):

        db = self.client[f"{self.DataBase}"]


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
            
            
    def calificaciones_tabla(self):

        db = self.client[f"{self.DataBase}"]

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


    def execute_function(self,user_input):

        options = {
            "calificaciones":self.calificaciones_tabla,
            "materias":self.Materias_tabla,
            "profesores":self.profesores_tabla
        }

        selected_function = options.get(user_input.lower())

        if selected_function:
            selected_function()
        else:
            print("Invalid Option")
