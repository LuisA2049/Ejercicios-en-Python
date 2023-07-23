#Set
cantidadpersonas = int(input("Cuantos nombres agregara? "))
personas = {}

i = 0

while i < cantidadpersonas:
    npersona = input("Cual es el nombre a agregar? ")
    personas[i+1] = npersona
    i += 1
    
print(personas)