import tkinter as tk

def on_text_changed(event):
    text.delete(1.0, tk.END)
    text.insert(tk.END, textbox.get())

root = tk.Tk()
root.title("Escribir en textbox")

label = tk.Label(root, text="Escribe algo en el textbox:")
label.pack()

textbox = tk.Entry(root)
textbox.pack()

button = tk.Button(root, text="Copiar", command=lambda: on_text_changed(None))
button.pack()

text = tk.Text(root, font= "Atlantis")
text.pack()

root.mainloop()
