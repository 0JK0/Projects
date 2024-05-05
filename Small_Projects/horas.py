

filename = "save.txt" # Just the easiest way i figured out to save information 

with open(filename,"r") as file:
    acumuladas = int(file.read())
    file.close()

print(acumuladas)

print("Llevas ",acumuladas," Horas acumuladas")

sumar = int(input("cuantas horas mas has hecho?: "))


acumuladas += sumar 

with open(filename,"w") as file:
    file.write(str(acumuladas))
    file.close()



print (acumuladas)
