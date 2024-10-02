from Ventanas.Ventana_interfaz import New_ventana
from util.colores import *
import sqlite3
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox  # Importamos la librería para la messagebox
from datetime import datetime

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

         # botones vaso de agua
         boton_v_1 = ctk.CTkButton(self.sub, text="", width=50, height=50, corner_radius=20, fg_color="gray", 
                                   command=lambda: self.toggle_color(0))
         boton_v_1.place(x=50, y=400)
         self.botones.append(boton_v_1)

         boton_v_2 = ctk.CTkButton(self.sub, text="", width=50, height=50, corner_radius=20, fg_color="gray", 
                                   command=lambda:  self.toggle_color(1) if self.estado_botones[0] else None)
         boton_v_2.place(x=110, y=400)
         self.botones.append(boton_v_2)

         boton_v_3 = ctk.CTkButton(self.sub, text="", width=50, height=50, corner_radius=20, fg_color="gray", 
                                   command=lambda: self.toggle_color(2) if self.estado_botones[1] else None)
         boton_v_3.place(x=170, y=400)
         self.botones.append(boton_v_3)

         boton_v_4 = ctk.CTkButton(self.sub, text="", width=50, height=50, corner_radius=20, fg_color="gray", 
                                   command=lambda: self.toggle_color(3) if self.estado_botones[2] else None)
         boton_v_4.place(x=230, y=400)
         self.botones.append(boton_v_4)

         boton_v_5 = ctk.CTkButton(self.sub, text="", width=50, height=50, corner_radius=20, fg_color="gray", 
                                   command=lambda: self.toggle_color(4) if self.estado_botones[3] else None)
         boton_v_5.place(x=290, y=400)
         self.botones.append(boton_v_5)

         boton_v_6 = ctk.CTkButton(self.sub, text="", width=50, height=50, corner_radius=20, fg_color="gray", 
                                   command=lambda: self.toggle_color(5) if self.estado_botones[4] else None)
         boton_v_6.place(x=350, y=400)
         self.botones.append(boton_v_6)

         boton_v_7 = ctk.CTkButton(self.sub, text="", width=50, height=50, corner_radius=20, fg_color="gray", 
                                   command=lambda: self.toggle_color(6) if self.estado_botones[5] else None)
         boton_v_7.place(x=410, y=400)
         self.botones.append(boton_v_7)

         boton_v_8 = ctk.CTkButton(self.sub, text="", width=50, height=50, corner_radius=20, fg_color="gray", 
                                   command=lambda: self.toggle_color(7) if self.estado_botones[6] else None)
         boton_v_8.place(x=470, y=400)
         self.botones.append(boton_v_8)

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

             self.Insertar_vasitos()

    def Insertar_vasitos(self):
        conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
        cursor = conn.cursor()
    
        fecha_actual = datetime.now().strftime("%Y-%m-%d")
    
        cursor.execute("SELECT cant FROM agua WHERE fecha = ?", (fecha_actual,))
        resultado = cursor.fetchone()
    
        if resultado:  
            nueva_cantidad = resultado[0] + 1
            cursor.execute("UPDATE agua SET cant = ? WHERE fecha = ?", (nueva_cantidad, fecha_actual))
        else:  
            cursor.execute("INSERT INTO agua (fecha, cant) VALUES (?, 1)", (fecha_actual,))
    
        conn.commit()
        conn.close()
