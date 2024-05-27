import json

def profesores_tabla():
    nombre = input("Insert the name: ")
    edad = input("Insert the age: ")
    genero = input("Insert the gender: ")
    fecha_nacimiento = input("Insert the birthday: ")
    titulo = input("Insert the title: ")
    materia = input("Insert the class: ")

    data_fill = [
        {"NOMBRE": nombre,
         "EDAD": edad,
         "GÉNERO": genero,
         "FECHA_NACIMIENTO": fecha_nacimiento,
         "TITULO": titulo,
         "MATERIA": materia}
    ]

    with open("demo_insert.json", "a") as jf:
        json.dump(data_fill, jf)
        jf.write('\n')  # Add a newline after each entry for readability
            

profesores_tabla()


