import tkinter as tk

letras_personalizadas = ["ᔑ", "ʖ", "ᓵ", "↸", "ᒷ", "⎓", "⊣", "⍑", "ꖎ", "⋮", "ꖌ", "ꖎ", "ᒲ", "リ", "¶", "𝙹", "!", "ᑑ", "∷", "ᓭ", "ℸ", "⚍", "⍊", "∴", "ß", "|", "⨅"]
abecedario_estadounidense = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def cifrar_mensaje():
    mensaje_original = entrada.get().upper()
    mensaje_cifrado = ""
    desplazamiento = int(desplazamiento_var.get())
    
    for letra in mensaje_original:
        if letra in abecedario_estadounidense:
            indice = abecedario_estadounidense.index(letra)
            letra_cifrada = letras_personalizadas[(indice + desplazamiento) % len(letras_personalizadas)]
            mensaje_cifrado += letra_cifrada
        else:
            mensaje_cifrado += letra
    
    salida.config(state="normal")
    salida.delete("1.0", tk.END)
    salida.insert(tk.END, mensaje_cifrado)
    salida.config(state="disabled")

def descifrar_mensaje():
    mensaje_cifrado = entrada1.get().upper()
    mensaje_descifrado = ""
    desplazamiento = int(desplazamiento_var.get())
    
    for letra in mensaje_cifrado:
        if letra in letras_personalizadas:
            indice = letras_personalizadas.index(letra)
            letra_descifrada = abecedario_estadounidense[(indice - desplazamiento) % len(abecedario_estadounidense)]
            mensaje_descifrado += letra_descifrada
        else:
            mensaje_descifrado += letra
    
    salida.config(state="normal")
    salida.delete("1.0", tk.END)
    salida.insert(tk.END, mensaje_descifrado)
    salida.config(state="disabled")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Cifrado César")
ventana.geometry("400x300")

# Etiqueta y entrada para el mensaje original
etiqueta_entrada = tk.Label(ventana, text="Mensaje original:")
etiqueta_entrada.pack()
entrada = tk.Entry(ventana)
entrada.pack()

# Etiqueta y entrada para el desplazamiento
etiqueta_desplazamiento = tk.Label(ventana, text="Desplazamiento:")
etiqueta_desplazamiento.pack()
desplazamiento_var = tk.StringVar()
desplazamiento_var.set("")
desplazamiento_entrada = tk.Entry(ventana, textvariable=desplazamiento_var)
desplazamiento_entrada.pack()

etiqueta_entrada1 = tk.Label(ventana, text="Mensaje a descifrar:")
etiqueta_entrada1.pack()
entrada1 = tk.Entry(ventana)
entrada1.pack()


# Botón para cifrar el mensaje
boton_cifrar = tk.Button(ventana, text="Cifrar", command=cifrar_mensaje)
boton_cifrar.pack()

# Botón para descifrar el mensaje
boton_descifrar = tk.Button(ventana, text="Descifrar", command=descifrar_mensaje)
boton_descifrar.pack()

# Área de texto para mostrar el mensaje cifrado o descifrado
salida = tk.Text(ventana, height=6, width=40, state="disabled")
salida.pack()

salida1 = tk.Text(ventana, height=6, width=40, state="disabled")
salida1.pack()


# Ejecutar la ventana
ventana.mainloop()
