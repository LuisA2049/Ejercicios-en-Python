from io import open
import pathlib
import shutil #modulo para archivos 

#mover
rutaOrigial=str(pathlib.Path().absolute())+"/4. Manejo de archivos/documento.txt "
rutaNueva=str(pathlib.Path().absolute())+"/4. Manejo de archivos/documentoCopiado.txt "
shutil.move(rutaOrigial,rutaNueva)