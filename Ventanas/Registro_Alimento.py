import customtkinter as ctk
from tkinter import Listbox
import sqlite3
from CTkMessagebox import CTkMessagebox
from util.colores import *
from Ventanas.Ventana_interfaz import New_ventana
from datetime import datetime

class Registro_Alimento(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)
        
        # Mostrar la ventana de alerta cada vez que se ingresa a esta sección
        self.mostrar_ventana_alerta()

        # Continuar con la configuración de la interfaz
        self.add_widget_registro()
        self.cargar_alimentos()
        self.update_coincidencias()
        
        ultimo_alimento = self.get_ultimo_insertado() # Se inicia en el constructor para que siempre se muestre :)
        self.label_segundo_registro.configure(text=ultimo_alimento)
        total_calorias = self.calcular_calorias_totales() # lo mismo que el anterior pero para el total de calorías
        self.label_total_c_mostrar.configure(text=total_calorias)

    def mostrar_ventana_alerta(self):
        # Texto introductorio para la sección "Registrar alimento"
        mensaje = (
            "Bienvenido a la sección 'Registrar alimento'. Aquí puedes buscar y seleccionar "
            "alimentos desde una base de datos, o ingresar uno nuevo manualmente. También "
            "puedes registrar las calorías consumidas y llevar un control del total diario."
        )
        CTkMessagebox(title="Registrar alimento", message=mensaje, icon="info", option_1="Ok")

    def add_widget_registro(self):
        self.label_agregar = ctk.CTkLabel(self.sub, text="Agregar alimento", text_color="white", bg_color=azul_medio_oscuro, font=("Arial", 20))
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
        self.label_buscar = ctk.CTkLabel(self.sub, text="Buscador de alimentos", text_color="white", bg_color=azul_medio_oscuro, font=("Arial", 20))
        self.label_buscar.place(relx=0.1, rely=0.30, relwidth=0.3, relheight=0.055)

        # Entry "Buscar alimento"
        self.entry_buscar = ctk.CTkEntry(self.sub, corner_radius=0, placeholder_text="Buscar alimento", 
                                         placeholder_text_color="black", border_width=0, fg_color="white", 
                                         text_color="black") 
        self.entry_buscar.place(relx=0.1, rely=0.35, relwidth=0.3) 
        self.entry_buscar.bind('<KeyRelease>', self.obtener_busqueda)

        # ListBox para coincidencias de búsqueda
        self.coincidencias = Listbox(self.sub)
        self.coincidencias.place(relx=0.1, relwidth=0.3, relheight=0.055, rely=0.4)
        self.coincidencias.bind('<<ListboxSelect>>', self.rellenar)


    def add_widget_registro(self):
        self.label_agregar = ctk.CTkLabel(self.sub, text="Agregar alimento", text_color="white", bg_color=azul_medio_oscuro, font=("Arial", 20))
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
        self.label_buscar = ctk.CTkLabel(self.sub, text="Buscador de alimentos", text_color="white", bg_color=azul_medio_oscuro, font=("Arial", 20))
        self.label_buscar.place(relx=0.1, rely=0.30, relwidth=0.3, relheight=0.055)

        # Entry "Buscar alimento"
        self.entry_buscar = ctk.CTkEntry(self.sub, corner_radius=0, placeholder_text="Buscar alimento", 
                                         placeholder_text_color="black", border_width=0, fg_color="white", 
                                         text_color="black") 
        self.entry_buscar.place(relx=0.1, rely=0.35, relwidth=0.3) 
        self.entry_buscar.bind('<KeyRelease>', self.obtener_busqueda)

        # ListBox para coincidencias de búsqueda
        self.coincidencias = Listbox(self.sub)
        self.coincidencias.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.055)
        self.coincidencias.bind('<<ListboxSelect>>', self.rellenar)

        self.alimentos_buscar = self.cargar_alimentos()
        self.match = []

        # Registro de último alimento
        self.label_registro = ctk.CTkLabel(self.sub, text="Último alimento registrado: ", text_color="white", 
                                           bg_color="#183549", font=("Arial", 20))
        self.label_registro.place(relx=0.5, rely=0.1, relwidth=0.4, relheight=0.055)

        # Ajustamos el tamaño y posición del segundo registro
        self.label_segundo_registro = ctk.CTkLabel(self.sub, text="", text_color="white", bg_color="#1f2329", font=("Arial", 20))
        self.label_segundo_registro.place(relx=0.5, rely=0.15, relwidth=0.4, relheight=0.055)
        
        # Label para calorías
        self.label_calorias = ctk.CTkLabel(self.sub, text="Calorías", text_color="white", 
                                           font=("Arial", 20), bg_color=azul_medio_oscuro)
        self.label_calorias.place(relx=0.1, rely=0.50, relwidth=0.3, relheight=0.05)

        # Entry para calorías
        self.entry = ctk.CTkEntry(self.sub, corner_radius=0, placeholder_text="Ingrese kcal consumidas", 
                                  placeholder_text_color="black", border_width=0, fg_color="white", 
                                  text_color="black") 
        self.entry.place(relx=0.1, rely=0.55, relwidth=0.3)


        # Botón "Registrar"
        self.boton_registrar = ctk.CTkButton(self.sub, text="Registrar", text_color="white", fg_color=azul_medio_oscuro, 
                                             hover_color=celeste_pero_oscuro, command=self.boton_mensanjes_insert, font=("Arial", 20))
        self.boton_registrar.place(relx=0.1, rely=0.73, relwidth=0.3, relheight=0.085)

        # Etiqueta para mostrar el total de calorías consumidas en el día
        self.label_total_calorias = ctk.CTkLabel(self.sub, text="Total calorías del día: 0", text_color="white", 
                                                 bg_color=azul_medio_oscuro, font=("Arial", 20))

        self.label_total_calorias = ctk.CTkLabel(self.sub, text="Total calorías del día: ", text_color="white", 
                                                 bg_color="#183549", font=("Arial", 20))

        self.label_total_calorias.place(relx=0.5, rely=0.35, relwidth=0.4, relheight=0.055)

        # Segundo label, muestra el total de calorias
        self.label_total_c_mostrar = ctk.CTkLabel(self.sub, text="", text_color="white",
                                                  bg_color="#1f2329", font=("Arial", 20))
        self.label_total_c_mostrar.place(relx=0.5, rely=0.40, relwidth=0.4, relheight=0.055)


    def cargar_alimentos(self):
        conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
        cursor = conn.cursor()

        # Obtener todos los nombres de alimentos
        cursor.execute("SELECT nombre FROM alimento")
        alimentos = cursor.fetchall()

        # Crear una lista de nombres de alimentos, excluyendo valores nulos
        lista_alimentos = [alimento[0] for alimento in alimentos if alimento[0] is not None]
        
        conn.close()
        return lista_alimentos


    def update_coincidencias(self):
        self.coincidencias.delete(0, ctk.END)
        num_coincidencias = len(self.match)

        if num_coincidencias > 0:
            height = min(num_coincidencias, 5)
            self.coincidencias.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.05 * height)
        else:
            self.coincidencias.place_forget()

        for alimento in self.match:
            self.coincidencias.insert(ctk.END, alimento)

    def rellenar(self, e):
        # Obtener el alimento seleccionado de la lista de coincidencias
        alimento_seleccionado = self.coincidencias.get(ctk.ACTIVE)
    
        # Actualizar el campo de entrada con el alimento seleccionado
        self.entry_buscar.delete(0, ctk.END)
        self.entry_buscar.insert(0, alimento_seleccionado)
    
        # Llamar a la lógica de selección de alimento (como lo haces con el ComboBox)
        self.on_alimento_select(alimento_seleccionado)

    def obtener_busqueda(self, e):
        typeado = self.entry_buscar.get()
        if not typeado or typeado == '':
            self.alimentos_buscar = ''
            self.match = []
        else: 
            self.alimentos_buscar = self.cargar_alimentos()
            self.match = [i for i in self.alimentos_buscar if typeado.lower() in i.lower()]
        self.update_coincidencias()

    def boton_mensanjes_insert(self):
        self.insert_alimento()        
        self.boton_registrar_click()  
        self.actualizar_calorias_totales()  # Llamamos a la nueva función

    def boton_registrar_click(self):
        alimento_seleccionado = self.combo_box.get()
        alimento_entry = self.entry_buscar.get().strip()
        calorias_ingresadas = self.entry.get().strip()
        
        print(f"Alimento seleccionado del ComboBox: {alimento_seleccionado}")  # Depuracion waza

        if alimento_seleccionado != "Seleccionar alimento":
            alimento = alimento_seleccionado
        elif alimento_entry:
            alimento = alimento_entry
        else:
            CTkMessagebox(title="Advertencia", message="Por favor, selecciona un alimento o ingresa uno válido.", icon='warning', option_1="Ok")
            return

        alimento_info = self.buscar_alimento_en_db(alimento)

        if alimento_info:
            nombre = alimento_info
            self.label_registro.configure(text=f"Último alimento registrado: {nombre}", font=("Arial", 14))
            # Eliminamos la distinción entre porción y 100g
            self.label_segundo_registro.configure(text=f"Calorías totales: {calorias_ingresadas}")
            self.combo_box.set("Seleccionar alimento")
            self.entry_buscar.delete(0, "end")
        else:
            CTkMessagebox(title="Alimento no encontrado", message="No se encontró el alimento en la base de datos.", icon='warning', option_1="Ok")

    def buscar_alimento_en_db(self, nombre_alimento):
        conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
        cursor = conn.cursor()
        query = "SELECT nombre, calorias_100gr, calorias_porcion FROM alimento WHERE nombre = ?"
        cursor.execute(query, (nombre_alimento,))
        resultado = cursor.fetchone()
        conn.close()
        return resultado

    def actualizar_calorias_totales(self):
        total_calorias = self.calcular_calorias_totales()
        self.label_total_c_mostrar.configure(text=total_calorias)

    def calcular_calorias_totales(self):
        conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
        cursor = conn.cursor()
        fecha_actual = datetime.now().strftime('%d-%m-%Y')
        query = '''
        SELECT SUM(total_cal) FROM consumo_diario WHERE fecha = ?
        '''
        cursor.execute(query, (fecha_actual,))
        resultado = cursor.fetchone()[0]
        conn.close()
        return resultado if resultado else 0

    def insert_alimento(self):
        conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
        cursor = conn.cursor()

        insert_query = '''
        INSERT INTO consumo_diario (nombre, fecha, hora, cantidad, total_cal) 
        VALUES (?, ?, ?, ?, ?);
        '''

        update_query = '''
        UPDATE consumo_diario 
        SET cantidad = cantidad + ?, total_cal = total_cal + ?
        WHERE nombre = ? AND fecha = ?;
        '''
        
        hora_actual = datetime.now().strftime('%H:%M:%S')
        fecha_actual = datetime.now().strftime('%d-%m-%Y')

        # Default quantity
        cantidad = 1

        # Obtener el alimento seleccionado del combobox o ingresado manualmente
        alimento_seleccionado = self.combo_box.get()  
        alimento_entry = self.entry_buscar.get().strip()
        alimento = alimento_seleccionado if alimento_seleccionado != "Seleccionar alimento" else alimento_entry
        
        # Verificar si el alimento existe en la base de datos
        alimento_info = self.buscar_alimento_en_db(alimento)

        if alimento_info:
            nombre, calorias_100g, calorias_porcion = alimento_info
            
            # Ahora tomamos las calorías directamente del campo de entrada (Entry)
            try:
                calorias = float(self.entry.get())  # El campo entry ya contiene las calorías
            except ValueError:
                CTkMessagebox(title="Error", message="Por favor, ingrese un valor de calorías válido.", icon='warning', option_1="Ok")
                return

            # Comprobar si el alimento ya fue registrado hoy
            cursor.execute('SELECT cantidad, total_cal FROM consumo_diario WHERE nombre = ? AND fecha = ?', (alimento, fecha_actual))
            resultado = cursor.fetchone()

            if resultado:
                # Si el alimento ya existe, actualizar la cantidad y total de calorías
                cursor.execute(update_query, (cantidad, calorias, alimento, fecha_actual))
            else:
                # Si el alimento no existe, insertarlo con cantidad = 1 y total_cal
                cursor.execute(insert_query, (alimento, fecha_actual, hora_actual, cantidad, calorias))

            conn.commit()
            CTkMessagebox(title="Registro exitoso", message=f"Alimento {alimento} registrado con éxito.", icon='info', option_1="Ok")
        else:
            CTkMessagebox(title="Alimento no encontrado", message="No se encontró el alimento en la base de datos.", icon='warning', option_1="Ok")
        
        conn.close()
        