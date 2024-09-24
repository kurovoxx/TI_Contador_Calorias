import customtkinter as ctk

# Configuración de la ventana principal
ctk.set_appearance_mode("light")  # Tema claro
ctk.set_default_color_theme("green")  # Tema verde

root = ctk.CTk()  # Crear la ventana principal
root.geometry("600x400")  # Tamaño de la ventana
root.title("Módulo de Salud")

# Creación de los botones "Actualizar Peso" y "Medir pulsaciones"
boton_peso = ctk.CTkButton(root, text="Actualizar Peso", width=150, height=50, fg_color="gray")
boton_peso.grid(row=0, column=0, padx=10, pady=10)  # Posicionar el botón "Actualizar Peso"

boton_pulsaciones = ctk.CTkButton(root, text="Medir pulsaciones", width=150, height=50, fg_color="gray")
boton_pulsaciones.grid(row=1, column=0, padx=10, pady=10)  # Posicionar el botón "Medir pulsaciones"

# Creación de los botones "IMC" y "*IMC"
boton_imc = ctk.CTkButton(root, text="IMC", width=75, height=50, fg_color="gray")
boton_imc.grid(row=0, column=1, padx=5, pady=10)  # Posicionar el botón "IMC"

boton_imc_rojo = ctk.CTkButton(root, text="*IMC", width=75, height=50, fg_color="red")
boton_imc_rojo.grid(row=0, column=2, padx=5, pady=10)  # Posicionar el botón "*IMC"

# Creación de los botones "IBR" y "*IBR"
boton_ibr = ctk.CTkButton(root, text="IBR", width=75, height=50, fg_color="gray")
boton_ibr.grid(row=1, column=1, padx=5, pady=10)  # Posicionar el botón "IBR"

boton_ibr_rojo = ctk.CTkButton(root, text="*IBR", width=75, height=50, fg_color="red")
boton_ibr_rojo.grid(row=1, column=2, padx=5, pady=10)  # Posicionar el botón "*IBR"

# Etiquetas de información (Meta de calorías y Vasos de agua)
label_calorias = ctk.CTkLabel(root, text="Meta de Calorías\nx/Meta", text_color="black")
label_calorias.grid(row=2, column=9, padx=20, pady=10)

label_agua = ctk.CTkLabel(root, text="Vasos de Agua: x", text_color="black")
label_agua.grid(row=3, column=9, padx=20, pady=10)

# Ejecutar la ventana
root.mainloop()
