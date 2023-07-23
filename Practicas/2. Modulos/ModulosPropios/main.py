#Accediendo a un modulo
#import operaciones

#print (operaciones.calculadora(7,5,"suma"))

#Para acceder sin anteponer el nombre del modulo
from operaciones import *

print (calculadora(7,5,"suma"))