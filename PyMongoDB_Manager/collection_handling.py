"""
Collection handling module for PyMongoDB Manager. 
This module defines the collections class that provides methods to interact with various collections within a MongoDB database.
"""

import json
import pymongo

class collections:

    """
    A class used to represent and interact with collections in a MongoDB database.

    Attributes:
        DataBase (str): The name of the database to interact with.
    """

    def __init__(self,DataBase):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.DataBase = DataBase


    def profesores_tabla(self):
        # Inserts new documents into the 'Profesores' collection based on user input.
        
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
        """
        Executes a function based on user input.

        Args:
            user_input (str): The user's choice of collection to interact with.
        """

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

    def new_structure(self,Coll):

        """
        Allows the user to make an entry for the choosen database and collection, using personalized camps.

        Args:
            Coll (str): The collection that is going to be used

        Returns:
            None

        """

        db = self.client[f"{self.DataBase}"]

        new_structure_list = [] 
        new_structure_collection = db[Coll]

        print("Write the camps you want to use separated by spaces. ") 
        camps = input("--> ").split()
        
        while True:
            
            data_fill = {}
            
            for camp in camps:
                value = input(f"Ingresa el {camp} : ")
                data_fill[camp] = value

            new_structure_list.append(data_fill)  
            
        
            continuar = input("Continuar ingresando? (si/no): ").lower()
            if continuar!= 'si':
                print(data_fill,new_structure_list)
                break

        with open("insert_personalized_structure.json", "w") as jf:
            json.dump(new_structure_list, jf)

        new_structure_collection.insert_many(new_structure_list)