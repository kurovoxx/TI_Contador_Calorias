import customtkinter as ctk
import tkinter as tk
import sqlite3
import openai
from CTkMessagebox import CTkMessagebox
from util.colores import *
from Ventanas.Ventana_interfaz import New_ventana
from datetime import datetime


class Registro_Alimento(New_ventana):
    OBJETIVO_DIARIO_CALORIAS = 2000  # Definir el objetivo diario de calorías

    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)
        self.add_widget_registro()
        self.cargar_alimentos()
        self.update_coincidencias()

    def add_widget_registro(self):
        self.label_agregar = ctk.CTkLabel(self.sub, text="Agregar alimento", text_color="white", bg_color='black', font=("Arial", 20))
        self.label_agregar.place(relx=0.1, rely=0.10, relwidth=0.3, relheight=0.05)

        # ComboBox dinámico, será llenado desde la base de datos
        self.combo_box = ctk.CTkComboBox(self.sub, corner_radius=0, fg_color="#183549",
                                         values=self.cargar_alimentos(),
                                         border_width=0, button_color="#26656D",
                                         button_hover_color="white", text_color="white")
        self.combo_box.place(relx=0.1, rely=0.15, relwidth=0.3, relheight=0.05)

        # Mensaje "predeterminado" para el combobox
        self.combo_box.set("Seleccionar alimento")  

        # Label "Buscador de alimentos"
        self.label_buscar = ctk.CTkLabel(self.sub, text="Buscador de alimentos", text_color="white", bg_color='black', font=("Arial", 20))
        self.label_buscar.place(relx=0.1, rely=0.30, relwidth=0.3, relheight=0.055)

        # Entry "Buscar alimento" que también estará vinculado a la búsqueda
        self.entry_buscar = ctk.CTkEntry(self.sub, corner_radius=0, placeholder_text="Buscar alimento", 
                                         placeholder_text_color="black", border_width=0, fg_color="white", 
                                         text_color="black") 
        self.entry_buscar.place(relx=0.1, rely=0.35, relwidth=0.3) 
        self.entry_buscar.bind('<KeyRelease>', self.obtener_busqueda)

        # ListBox para coincidencias de búsqueda
        self.coincidencias = tk.Listbox(self.sub)
        self.coincidencias.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.055)
        self.coincidencias.bind('<<ListboxSelect>>', self.rellenar)

        self.alimentos_buscar = self.cargar_alimentos()
        self.match = []

        # Registro de último alimento
        self.label_registro = ctk.CTkLabel(self.sub, text="Último alimento registrado: ", text_color="white", 
                                           bg_color="#183549", font=("Arial", 20))
        self.label_registro.place(relx=0.5, rely=0.1, relwidth=0.4, relheight=0.055)

        self.label_segundo_registro = ctk.CTkLabel(self.sub, text="", text_color="white", bg_color="#1f2329", font=("Arial", 20))
        self.label_segundo_registro.place(relx=0.5, relwidth=0.4, relheight=0.055, rely=0.15)

        # Corrección para mostrar el Label y Entry al cambiar la opción del ComboBox
        self.combo_box_b = ctk.CTkComboBox(self.sub, corner_radius=0, fg_color="#183549",
                                           values=["Por 100gr", "Por porcion"],
                                           border_width=0, button_color="#26656D",
                                           button_hover_color="white", text_color="white",
                                           command=self.aparecer_label)  # Se debe agregar el 'command'
        self.combo_box_b.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.06)

        self.label = ctk.CTkLabel(self.sub, text="", text_color="white", bg_color=COLOR_BOTON2, font=("Arial", 20))
        self.entry = ctk.CTkEntry(self.sub, corner_radius=0, placeholder_text="Ingrese kcal consumidas", 
                                         placeholder_text_color="black", border_width=0, fg_color="white", 
                                         text_color="black") 

        # Botón "Registrar"
        self.boton_registrar = ctk.CTkButton(self.sub, text="Registrar", text_color="white", fg_color=COLOR_BOTON2, 
                                              command=self.boton_mensanjes_insert, font=("Arial", 20))
        self.boton_registrar.place(relx=0.1, rely=0.77, relwidth=0.3, relheight=0.085)

        self.label_agregar = ctk.CTkLabel(self.sub, text="Calorias del dia", text_color="white", bg_color='#183549', font=("Arial", 20))
        self.label_agregar.place(relx=0.5, rely=0.3, relwidth=0.4, relheight=0.055)

        self.label_total_calorias = ctk.CTkLabel(self.sub, text="Total calorías del día: 0", text_color="white", 
                                                 bg_color="#1f2329", font=("Arial", 20))
        self.label_total_calorias.place(relx=0.5, rely=0.35, relwidth=0.4, relheight=0.055)

        # Label "Calorías recomendadas del día"
        self.label_calorias_recomendadas = ctk.CTkLabel(self.sub, text="Calorías recomendadas del día", text_color="white", 
                                                        bg_color='#183549', font=("Arial", 18))
        self.label_calorias_recomendadas.place(relx=0.5, rely=0.42, relwidth=0.4, relheight=0.04)

        # Barra de progreso de calorías
        self.barra_progreso_calorias = ctk.CTkProgressBar(self.sub, fg_color="#183549", progress_color="#26656D")
        self.barra_progreso_calorias.place(relx=0.5, rely=0.47, relwidth=0.4, relheight=0.05)
        self.barra_progreso_calorias.set(0)  # Inicialmente vacío

        # Añadir un campo de entrada para la hora de registro
        self.label_hora = ctk.CTkLabel(self.sub, text="Hora (HH:MM):", text_color="white", bg_color='black', font=("Arial", 14))
        self.label_hora.place(relx=0.1, rely=0.65, relwidth=0.3, relheight=0.04)

        self.entry_hora = ctk.CTkEntry(self.sub, corner_radius=0, placeholder_text="Ingrese hora (opcional)", 
                                       placeholder_text_color="gray", border_width=0, fg_color="white", 
                                       text_color="black")
        self.entry_hora.place(relx=0.1, rely=0.70, relwidth=0.3, relheight=0.05)

        # Label y Botón de IA:
        consejo_guardado = self.cargar_consejo_desde_archivo()

        # Label para el consejo del día
        self.label_consejo = ctk.CTkLabel(self.sub, text=f"Consejo del día ({datetime.now().strftime('%d-%m-%Y')}):", 
                                          text_color="white", bg_color='#404B4C', font=("Arial", 16), wraplength=300)
        self.label_consejo.place(relx=0.4, rely=0.7, relwidth=0.8)
    
        # Botón para generar el consejo del día
        self.boton_generar = ctk.CTkButton(self.sub, text="Generar Consejo Saludable", text_color="white",
                                           command=self.mostrar_consejo, fg_color=COLOR_BOTON2)
        self.boton_generar.place(relx=0.6, rely=0.63, relwidth=0.4, relheight=0.05)
        
        # Si ya existe un consejo, mostrarlo y deshabilitar el botón
        if consejo_guardado:
            self.label_consejo.configure(text=f"Consejo del día ({datetime.now().strftime('%d-%m-%Y')}): {consejo_guardado}")
            self.boton_generar.configure(state="disabled")

    def aparecer_label(self, selection):
        if selection == "Por 100gr":
            self.label.configure(text="100gr")
        elif selection == "Por porcion":
            self.label.configure(text="Porción")

        # Corregir las posiciones de los elementos
        self.label.place(relx=0.1, rely=0.5, relwidth=0.3, relheight=0.05)
        self.entry.place(relx=0.1, rely=0.55, relwidth=0.3)

    def obtener_busqueda(self, event):
        value = event.widget.get()
        value = value.strip().lower()

        if value == '':
            self.coincidencias.delete(0, tk.END)
            self.match = []
        else:
            self.match = [item for item in self.alimentos_buscar if value in item.lower()]
            self.coincidencias.delete(0, tk.END)

            for item in self.match:
                self.coincidencias.insert(tk.END, item)

    def rellenar(self, event):
        seleccion = self.coincidencias.curselection()

        if seleccion:
            alimento_seleccionado = self.match[seleccion[0]]
            self.entry_buscar.delete(0, tk.END)
            self.entry_buscar.insert(0, alimento_seleccionado)
            self.coincidencias.delete(0, tk.END)

    def insert_alimento(self):
        conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
        cursor = conn.cursor()
        query = '''
        INSERT INTO consumo_diario (nombre, fecha, hora, cantidad) VALUES (?, ?, ?, ?);
        '''

        # Obtener la hora ingresada por el usuario o usar la hora actual
        hora_ingresada = self.entry_hora.get().strip()
        hora_actual = hora_ingresada if hora_ingresada else datetime.now().strftime('%H:%M:%S')

        cantidad = self.entry.get()

        alimento_seleccionado = self.combo_box.get()
        alimento_entry = self.entry_buscar.get().strip()
        alimento = alimento_seleccionado if alimento_seleccionado != "Seleccionar alimento" else alimento_entry

        cursor.execute(query, (alimento, datetime.now().strftime('%d-%m-%Y'), hora_actual, cantidad))
        conn.commit()
        conn.close()

    def cargar_alimentos(self):
        conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
        cursor = conn.cursor()
        cursor.execute("SELECT nombre FROM consumo_diario")
        alimentos = cursor.fetchall()
        conn.close()
        return [alimento[0] for alimento in alimentos]

    def update_coincidencias(self):
        self.alimentos_buscar = self.cargar_alimentos()

    def boton_mensanjes_insert(self):
        # Lógica para mostrar mensaje
        self.insert_alimento()

    def mostrar_consejo(self):
        # Lógica de la función mostrar_consejo
        pass

    def cargar_consejo_desde_archivo(self):
        # Cargar el consejo desde el archivo
        return None
