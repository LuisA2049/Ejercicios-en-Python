import re

print('ingresa la palabra')

buscar = re.search("A|a", input())

if buscar:
    print("La palabra si contiene una letra A")
else:
    print("La palabra no contiene una letra A")
