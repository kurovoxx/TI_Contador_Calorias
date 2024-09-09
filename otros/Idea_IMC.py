import customtkinter as ctk

# Configuración de la apariencia y tema
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue") 

# Crear la ventana principal de la aplicación
app = ctk.CTk()
app.geometry("300x400")
app.title("Calculadora de IMC")


# Función para calcular el IMC
def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get()) / 100  # Convertir la altura a metros
        imc = peso / (altura ** 2)
        label_resultado.configure(text=f"Tu IMC es: {imc:.2f}")
    except ValueError:
        label_resultado.configure(text="Por favor, ingrese valores válidos.")

# Crear un frame para el formulario
frame_formulario = ctk.CTkFrame(master=app)
frame_formulario.pack(pady=20, padx=20, fill="both", expand=True)

# Crear un campo de entrada para la altura
label_altura = ctk.CTkLabel(master=frame_formulario, text="Altura (cm):")
label_altura.pack(pady=10, padx=10)
entry_altura = ctk.CTkEntry(master=frame_formulario)
entry_altura.pack(pady=10, padx=10)

# Crear un campo de entrada para el peso
label_peso = ctk.CTkLabel(master=frame_formulario, text="Peso (kg):")
label_peso.pack(pady=10, padx=10)
entry_peso = ctk.CTkEntry(master=frame_formulario)
entry_peso.pack(pady=10, padx=10)

# Crear un botón para calcular el IMC
boton_calcular = ctk.CTkButton(master=frame_formulario, text="Calcular IMC", command=calcular_imc)
boton_calcular.pack(pady=20, padx=10)

# Crear un label para mostrar el resultado
label_resultado = ctk.CTkLabel(master=frame_formulario, text="")
label_resultado.pack(pady=20, padx=10)

# Iniciar la aplicación
app.mainloop()
