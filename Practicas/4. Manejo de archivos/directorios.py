import os
import shutil
#Como crear una carpeta

if not  os.path.isdir("../miCarpeta"):
    os.mkdir("../miCarpeta")
else:
    print("El archivo existe")

#Eliminar
#os.rmdir('../miCarpeta')

#copiar
rutaOrigial="../miCarpeta"
rutaNueva="../carpetaCopiada "

shutil.copytree(rutaOrigial,rutaNueva)

#imprimir archivos que contiene una carpeta
print ("Contenido de la carpeta:")
contenido= os.listdir("../miCarpeta")
for fichero in contenido:
    print ("Fichero: "+fichero)