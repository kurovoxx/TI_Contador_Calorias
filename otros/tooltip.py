import tkinter as tk
from tktooltip import ToolTip

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Tooltip")

# Crear un botón
button = tk.Button(root, text="Pasa el mouse aquí")
button.pack(padx=200, pady=200)

# Agregar un tooltip
ToolTip(button, msg="Este es un tooltip de ejemplo")

# Iniciar el bucle principal
root.focus_force()
root.mainloop()
