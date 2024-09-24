import customtkinter as ctk

# Configuración de la ventana principal
ctk.set_appearance_mode("light")  # Tema claro
ctk.set_default_color_theme("green")  # Tema verde

root = ctk.CTk()  # Crear la ventana principal
root.geometry("400x200")  # Tamaño de la ventana
root.title("Botones Toggle")

# Crear una barra de progreso
progress_bar = ctk.CTkProgressBar(root, width=300, height=20, corner_radius=20)
progress_bar.grid(row=0, column=0, columnspan=8, pady=20)  # Posicionar la barra
progress_bar.set(0.5)  # Establecer el valor de la barra (50%)

# Función para alternar el color del botón
def toggle_color(boton):
    # Cambiar entre verde y gris
    if boton.cget("fg_color") == "gray":  # Si el botón está gris
        boton.configure(fg_color="green")  # Cambia a verde
    else:
        boton.configure(fg_color="gray")  # Cambia a gris

# Crear los 8 botones redondeados debajo de la barra
botones = []
for i in range(8):
    boton = ctk.CTkButton(root, text="", width=40, height=40, corner_radius=20, fg_color="gray", command=lambda b=i: toggle_color(botones[b]))
    boton.grid(row=1, column=i, padx=5, pady=10)  # Posicionar los botones
    botones.append(boton)

# Ejecutar la ventana
root.mainloop()
