import json

def profesores_tabla():
    while True:
        profesores_list = []
    
        nombre = input("Insert the name: ")
        edad = input("Insert the age: ")
        genero = input("Insert the gender: ")
        fecha_nacimiento = input("Insert the birthday: ")
        titulo = input("Insert the title: ")
        materia = input("Insert the class: ")

        data_fill = {
            "NOMBRE": nombre,
            "EDAD": edad,
            "GÉNERO": genero,
            "FECHA_NACIMIENTO": fecha_nacimiento,
            "TITULO": titulo,
            "MATERIA": materia}
    
        profesores_list.append(data_fill) 
    
        continuar = input("Do you want to continue? (yes/no): ").lower()
        if continuar!= 'yes':
             break
 

        with open("demo_insert.json", "a") as jf:
            json.dump(data_fill, jf)
            jf.write('\n') 
        
       
            


def Materias_tabla():
    materias_list = [] 
    
    while True:
        nombre = input("Insert the name: ")
        horas = input("Insert the Hours: ")
        grado = input("Insert the Grade: ")

        data_fill = {
            "NOMBRE_MATERIA": nombre,
            "HORAS": horas,
            "GRADO": grado
        }

        materias_list.append(data_fill)  
        
       
        continuar = input("Do you want to continue? (yes/no): ").lower()
        if continuar!= 'yes':
            break

    
    with open("demo_insert.json", "w") as jf:
        json.dump(materias_list, jf)
        
        
def calificaciones_tabla():
    calificaciones_list = [] 
    
    while True:
        nombre = input("Insert the name: ")
        grado= input("Insert the Grade: ")
        profesor = input("Insert the Professor: ")
        nota1 = input("Insert the 1st Note: ")
        nota2 = input("Insert the 2nd Note: ")
        nota3 = input("Insert the 3rd Note: ")
        definitiva = input("Insert the definitve: ")

        data_fill = {
            "NOMBRE_ESTUDIANTE": nombre,
            "GRADO": grado,
            "PROFESOR": profesor,
            "NOTA1":nota1,
            "NOTA2":nota2,
            "NOTA3":nota3,
            "DEFINITIVA":definitiva
        }

        calificaciones_list.append(data_fill)  
        
       
        continuar = input("Do you want to continue? (yes/no): ").lower()
        if continuar!= 'yes':
            break

    with open("demo_insert.json", "w") as jf:
        json.dump(calificaciones_list, jf)
        

    
    
uses = input("Table to use? \n 1.Profesores \n 2.Materias \n 3.Calificaiones \n ")

if uses == "1":
    profesores_tabla()
elif uses == "2":
    Materias_tabla()
elif uses == "3":
    calificaciones_tabla()



