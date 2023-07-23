#Diccionario
from os import system
cantidadpersonas = int(input("Cuantas personas agregara? "))
system("cls")
personas = {}

i = 0

while i < cantidadpersonas:
    nombre = input("Cual es el nombre de la persona? ")
    apellido = input("Cual es el apellido de la persona? ")
    telefono = int(input("Cual es el telefono de la persona? "))
    
    personas[i+1] = {"nombre": nombre, "apellido": apellido, "telefono": telefono}
    
    system("cls")

    i += 1
    
print(personas)