# Code para determinar el riesgo de padecer diabetes

import customtkinter as ctk

# Configuración de la apariencia y tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Crear la ventana principal de la aplicación
app = ctk.CTk()
app.geometry("400x500")
app.title("Detección de Riesgo de Cáncer")

# Función para calcular el riesgo basado en la entrada del usuario
def calcular_riesgo():
    try:
        glucosa = float(entry_glucosa.get())
        presion = float(entry_presion.get())
        imc = float(entry_imc.get())

        riesgo = sum([
            glucosa >= 126,
            presion >= 130,
            imc >= 30
        ])

        mensaje = [
            "Usted es saludable.",
            "Usted tiene un riesgo bajo de cáncer.",
            "Usted tiene un riesgo moderado de cáncer.",
            "Usted tiene un alto riesgo de cáncer."
        ]

        resultado_label.configure(text=mensaje[riesgo])
    except ValueError:
        resultado_label.configure(text="Por favor, ingrese valores numéricos válidos.")

# Etiquetas y entradas para los datos del usuario
label_glucosa = ctk.CTkLabel(app, text="Nivel de glucosa en ayunas (mg/dL):")
label_glucosa.pack(pady=10)

entry_glucosa = ctk.CTkEntry(app)
entry_glucosa.pack(pady=10)

label_presion = ctk.CTkLabel(app, text="Presión arterial sistólica (mmHg):")
label_presion.pack(pady=10)

entry_presion = ctk.CTkEntry(app)
entry_presion.pack(pady=10)

label_imc = ctk.CTkLabel(app, text="Índice de masa corporal (IMC):")
label_imc.pack(pady=10)

entry_imc = ctk.CTkEntry(app)
entry_imc.pack(pady=10)

# Botón para calcular el riesgo
calcular_button = ctk.CTkButton(app, text="Calcular Riesgo", command=calcular_riesgo)
calcular_button.pack(pady=20)

# Etiqueta para mostrar el resultado
resultado_label = ctk.CTkLabel(app, text="")
resultado_label.pack(pady=20)

# Iniciar la aplicación
app.mainloop()
