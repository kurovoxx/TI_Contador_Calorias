from Ventanas.Ventana_interfaz import New_ventana
from util.colores import *
import customtkinter as ctk

class Salud(New_ventana):
     def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)
        self.add_widget_salud()

     def add_widget_salud(self):
         # Botón "Actualizar Peso"
         btn_actualizar_peso = ctk.CTkButton(self, text="Actualizar Peso", width=150, height=50, fg_color="gray")
         btn_actualizar_peso.place(x=50, y=50)  # Colocar en la posición exacta

         # Botón "Medir pulsaciones"
         btn_medir_pulsaciones = ctk.CTkButton(self, text="Medir pulsaciones", width=150, height=50, fg_color="gray")
         btn_medir_pulsaciones.place(x=50, y=150)

         # Botón "IMC" y "*IMC"
         btn_imc = ctk.CTkButton(self, text="IMC", width=100, height=50, fg_color="gray")
         btn_imc.place(x=500, y=50)

         btn_imc_rojo = ctk.CTkButton(self, text="*IMC", width=100, height=50, fg_color="red")
         btn_imc_rojo.place(x=600, y=50)

         # Botón "IBR" y "*IBR"
         btn_ibr = ctk.CTkButton(self, text="IBR", width=100, height=50, fg_color="gray")
         btn_ibr.place(x=500, y=150)

         btn_ibr_rojo = ctk.CTkButton(self, text="*IBR", width=100, height=50, fg_color="red")
         btn_ibr_rojo.place(x=600, y=150)

         # Crear los 8 botones redondeados debajo de la barra
         self.botones = []
         for i in range(8):
             boton = ctk.CTkButton(self, text="", width=50, height=50, corner_radius=20, fg_color="gray", command=lambda b=i: toggle_color(botones[b]))
             boton.place(x=50 + i * 60, y=400)  # Posicionar los botones
             self.botones.append(boton)

         # Barra inferior
         barra_inferior = ctk.CTkProgressBar(self, width=550, height=40, fg_color="gray", progress_color="green")
         barra_inferior.place(x=20, y=350)
         barra_inferior.set(0.7)  # Ajuste del progreso 

         # Etiquetas de Meta de Calorías y Vasos de Agua
         label_meta_calorias = ctk.CTkLabel(self, text="Meta de Calorías x/Meta", fg_color=None, text_color="black", font=("Arial", 15))
         label_meta_calorias.place(x=600, y=350)

         label_vasos_agua = ctk.CTkLabel(self, text="Vasos de Agua: x", fg_color=None, text_color="black", font=("Arial", 15))
         label_vasos_agua.place(x=600, y=420)

# Función para alternar el color del botón
def toggle_color(boton):
    # Cambiar entre verde y gris
    if boton.cget("fg_color") == "gray":  # Si el botón está gris
        boton.configure(fg_color="green")  # Cambia a verde
    else:
        boton.configure(fg_color="gray")  # Cambia a gris

