
from io import open
import pathlib

#str(pathlib.Path().absolute())
#obtenemos la direccion del path para entrar a la carpeta del 
#archivo
ruta=str(pathlib.Path().absolute())+"/4. Manejo de archivos/documento.txt "
#Imprime la ruta del archivo
print (ruta)

#Apertura del archivo
archivo =open(ruta,"r")
#El a+ Significa el tipo  de apertura

#Leer contenido
#contenido=archivo.read()
#print (contenido)

#Leer contenido y guardarlo en lista
lista= archivo.readlines()
#Cerrar el archivo
archivo.close()

for elemento in lista:
  #  if elemento.isnumeric(): #Verificamos si es numero
      #  lista_frase=elemento.split() #convertir renglkon a lista
        print ("- "+elemento.upper()) #converite a mayuscula
