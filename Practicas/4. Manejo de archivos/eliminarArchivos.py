from genericpath import isfile
import os #Modulo para eliminar archivos
import pathlib




#comprobar si existe
import os.path

rutaComprobar=os.path.abspath("./")+"/ficheroTexto.txt"

if os.path.isfile(rutaComprobar):
    print ("El Archivo si existe")
    os.remove(rutaComprobar)
    #Con remove remueve el documento de la ruta seleccionada
else:
    print("El archivo no existe")
