from os import system

contactos = []
print(contactos)

numerocontactos = int(input("Cantidad de contactos a ingresar? "))

system("cls")

for x in range(numerocontactos):
    cts = {"Nombre": input("Ingresa el nombre: "), "Telefono": int(input("Ingresa el numero: "))}
    system("cls")
    contactos.append(cts)

system("cls")
print(contactos)
