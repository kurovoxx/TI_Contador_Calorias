import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from Ventanas.Ventana_interfaz import New_ventana


class Configuracion(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)
        self.add_widget_config()
        self.contruirWidget()

    def add_widget_config(self):
        #Titulo para el modulo configuración :)
        self.title_label = ctk.CTkLabel(self.sub, text="Actualizar informacion Usuario",text_color="white",font=("Arial", 27))
        self.title_label.pack(padx=20, pady=5, anchor="w")
        
        self.perfil_frame = ctk.CTkFrame(self.sub, width=300)
        self.perfil_frame.pack(padx=20, pady=10, anchor="w")

        self.nombre_label = ctk.CTkLabel(self.perfil_frame, text="Nombre:")
        self.nombre_label.pack(anchor="w", padx=3, pady=3)
        
        self.nombre_entry = ctk.CTkEntry(self.perfil_frame, placeholder_text="Introduce tu nombre", width=250)
        self.nombre_entry.pack(padx=3, pady=(0, 2))

        self.edad_label = ctk.CTkLabel(self.perfil_frame, text="Edad:")
        self.edad_label.pack(anchor="w", padx=3, pady=(2, 0))
        
        self.edad_entry = ctk.CTkEntry(self.perfil_frame, placeholder_text="Introduce tu edad", width=250)
        self.edad_entry.pack(padx=3, pady=(0, 2))

        self.gen_label = ctk.CTkLabel(self.perfil_frame, text="Sexo:")
        self.gen_label.pack(anchor="w", padx=3, pady=(2, 0))
        
        self.gen_combobox = ctk.CTkComboBox(self.perfil_frame, values=["Masculino", "Femenino", "Otro"], width=250)
        self.gen_combobox.pack(padx=3, pady=(0, 2))

        self.peso_label = ctk.CTkLabel(self.perfil_frame, text="Peso (kg):")
        self.peso_label.pack(anchor="w", padx=3, pady=(2, 0))
        
        self.peso_entry = ctk.CTkEntry(self.perfil_frame, placeholder_text="Introduce tu peso", width=250)
        self.peso_entry.pack(padx=3, pady=(0, 2))

        self.altura_label = ctk.CTkLabel(self.perfil_frame, text="Altura (cm):")
        self.altura_label.pack(anchor="w", padx=3, pady=(2, 0))
        
        self.altura_entry = ctk.CTkEntry(self.perfil_frame, placeholder_text="Introduce tu altura", width=250)
        self.altura_entry.pack(padx=3, pady=(0, 2))

        self.obj_calorias_label = ctk.CTkLabel(self.perfil_frame, text="Objetivo de Calorías:")
        self.obj_calorias_label.pack(anchor="w", padx=3, pady=(2, 0))
        
        self.obj_calorias_combobox = ctk.CTkComboBox(self.perfil_frame, values=["Pérdida de peso", "Mantenimiento", "Aumento de peso"], width=250)
        self.obj_calorias_combobox.pack(padx=3, pady=(0, 2))

        self.lvl_actividad_label = ctk.CTkLabel(self.perfil_frame, text="Nivel de Actividad:")
        self.lvl_actividad_label.pack(anchor="w", padx=3, pady=(2, 0))
        
        self.lvl_actividad_combobox = ctk.CTkComboBox(self.perfil_frame, values=["Sedentario", "Ligero", "Moderado", "Intenso"], width=250)
        self.lvl_actividad_combobox.pack(padx=3, pady=(0, 2))

        self.guardar_button = ctk.CTkButton(self.perfil_frame, text="Actualizar información", command=self.guardar, width=250)
        self.guardar_button.pack(pady=5)
        
    def guardar(self):
        try:
            with open("Configuracion.txt", "a") as archivo_n:
                nombre = self.nombre_entry.get()
                archivo_n.write(f'Nombre: {nombre}\n')

                edad = self.edad_entry.get()
                archivo_n.write(f'Edad: {edad}\n')

                sexo = self.gen_combobox.get()
                archivo_n.write(f'Genero: {sexo}\n')

                peso = self.peso_entry.get()
                archivo_n.write(f'Peso: {peso}\n')

                altura = self.altura_entry.get()
                archivo_n.write(f'Altura: {altura}\n')

                objetivo_calorias = self.obj_calorias_combobox.get()
                archivo_n.write(f'Objetivo: {objetivo_calorias}\n')

                nivel_actividad = self.lvl_actividad_combobox.get()
                archivo_n.write(f'Nivel de actividad: {nivel_actividad}\n')

            messagebox.showinfo("Confirmación", "Los datos se guardaron correctamente.")
            
        except FileNotFoundError:
            messagebox.showerror("Error", "Hubo un problema al guardar los datos.")

    def contruirWidget(self):
        self.info_frame = ctk.CTkFrame(self.sub, width=250)
        self.info_frame.pack(padx=20, pady=5, anchor="w")
        
        self.labelVersion = ctk.CTkLabel(self.info_frame, text="Version : 1.0", width=250)
        self.labelVersion.pack(pady=3)

        self.labelAutor = ctk.CTkLabel(self.info_frame, text="Autor : Los insanos 2.0", width=250)
        self.labelAutor.pack(pady=3)
