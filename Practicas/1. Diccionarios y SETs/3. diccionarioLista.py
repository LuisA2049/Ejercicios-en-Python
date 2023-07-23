#Usando listas con diccionarios
contactos=[
    {
        "nombre":"antonio",
        "telefono":"63155841"
    },
    {
        "nombre":"Manuel",
        "telefono":"12548647"
    }
]
#Cambio de dato
contactos[0]["nombre"]="Antonio"
print(contactos[0]["nombre"])

#impresion de nombres
print ("\n Lista de contactos")
for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")