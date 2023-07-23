import re

print("Ingrese el numero telefonico. Ejemplo: 637-376-2335")

validacion = re.search(r'\d{3}-\d{3}-\d{4}', input())

if validacion:
    print("Bien...")
else:
    print("Mal...")