from io import open
import pathlib

#str(pathlib.Path().absolute())
#obtenemos la direccion del path para entrar a la carpeta del 
#archivo
ruta=str(pathlib.Path().absolute())+"/4. Manejo de archivos/documento.txt "
#Imprime la ruta del archivo
print (ruta)

#Apertura del archivo
archivo =open(ruta,"a+")
#El a+ Significa el tipo  de apertura

#Escribir dentro del archivo
archivo.write("Agregamos datos desde python \n")
#Cerrar archivo
archivo.close()
