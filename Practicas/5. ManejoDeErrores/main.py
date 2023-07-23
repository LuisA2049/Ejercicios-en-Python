try:
    nombre= input("Ingresa tu nombre")
    if(len(nombre)>=3):
        nombre_usuario="El nombre de la persona es: "+nombre
    
    print(nombre_usuario)

except:
    print("Ha ocurrido un error al momento de ingresar el nombre")

else:
    print("Todo ha ocurrido muy bien")

finally:
    print("Fin del programa")