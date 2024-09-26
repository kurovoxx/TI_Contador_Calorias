from Ventanas.Ventana_interfaz import New_ventana
from util.colores import *
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox  # Importamos la librería para la messagebox

class Salud(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)
        self.mostrar_messagebox()  # Llamamos a la función que muestra el mensaje al abrir la pestaña
        self.add_widget_salud()

    # Función para mostrar la CTkMessagebox
    def mostrar_messagebox(self):
        mensaje = ("Bienvenido a la sección Salud. Aquí podrás actualizar tu peso, medir pulsaciones, "
                   "calcular tu IMC Y TMB, además de realizar un seguimiento de tu progreso diario. "
                   "Usa los botones y la barra de progreso para monitorear tus metas.")
        CTkMessagebox(title="Sección Salud", message=mensaje, icon="info", option_1="OK")

    def add_widget_salud(self):
         # Botón "Actualizar Peso"
         self.btn_actualizar_peso = ctk.CTkButton(self.sub, text="Actualizar Peso", width=150, height=50, fg_color="gray")
         self.btn_actualizar_peso.place(x=50, y=50)  # Colocar en la posición exacta

         # Botón "Medir pulsaciones"
         self.btn_medir_pulsaciones = ctk.CTkButton(self.sub, text="Medir pulsaciones", width=150, height=50, fg_color="gray")
         self.btn_medir_pulsaciones.place(x=50, y=150)

         # Botón "IMC" y "*IMC"
         self.btn_imc = ctk.CTkButton(self.sub, text="IMC", width=100, height=50, fg_color="gray")
         self.btn_imc.place(x=500, y=50)

         self.btn_imc_rojo = ctk.CTkButton(self.sub, text="*IMC", width=100, height=50, fg_color="red")
         self.btn_imc_rojo.place(x=600, y=50)

         # Botón "IBR" y "*IBR"
         self.btn_ibr = ctk.CTkButton(self.sub, text="IBR", width=100, height=50, fg_color="gray")
         self.btn_ibr.place(x=500, y=150)

         self.btn_ibr_rojo = ctk.CTkButton(self.sub, text="*IBR", width=100, height=50, fg_color="red")
         self.btn_ibr_rojo.place(x=600, y=150)

         # Crear los 8 botones redondeados debajo de la barra
         self.botones = []
         self.estado_botones = [False] * 8  # Lista para almacenar el estado de cada botón (False = gris, True = verde)

         for i in range(8):
             boton = ctk.CTkButton(self.sub, text="", width=50, height=50, corner_radius=20, fg_color="gray", 
                                   command=lambda b=i: self.toggle_color(b))
             boton.place(x=50 + i * 60, y=400)  # Posicionar los botones
             self.botones.append(boton)

         # Barra inferior
         self.barra_inferior = ctk.CTkProgressBar(self.sub, width=550, height=40, fg_color="gray", progress_color="green")
         self.barra_inferior.place(x=20, y=350)
         self.barra_inferior.set(0.7)  # Ajuste del progreso 

         # Etiquetas de Meta de Calorías y Vasos de Agua
         self.label_meta_calorias = ctk.CTkLabel(self.sub, text="Meta de Calorías x/Meta", fg_color=None, text_color="black", font=("Arial", 15))
         self.label_meta_calorias.place(x=600, y=350)

         self.label_vasos_agua = ctk.CTkLabel(self.sub, text="Vasos de Agua: x", fg_color=None, text_color="black", font=("Arial", 15))
         self.label_vasos_agua.place(x=600, y=420)

     # Nueva función para alternar el color y estado de los botones
    def toggle_color(self, indice):
         # Cambia el estado del botón (True = verde, False = gris)
         if self.estado_botones[indice]:  # Si el botón está activo (verde)
             self.botones[indice].configure(fg_color="gray")  # Cambiar a gris
             self.estado_botones[indice] = False  # Cambiar estado a inactivo
         else:  # Si el botón está inactivo (gris)
             self.botones[indice].configure(fg_color="green")  # Cambiar a verde
             self.estado_botones[indice] = True  # Cambiar estado a activo

