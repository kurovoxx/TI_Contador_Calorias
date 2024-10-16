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
        self.nombre = 'registrar_alimento'


        self.add_widget_registro()
        self.cargar_alimentos()
        self.update_coincidencias()
        self.mensage("En esta pestaña, puedes registrar los alimentos consumidos durante el día y las calorías totales. Primero, debes añadir el alimento en la pestaña Agregar Alimento. Luego, podrás buscarlo con un buscador o ver todos los alimentos registrados.", "Registrar Alimento")
        ultimo_alimento = self.get_ultimo_insertado() # Se inicia en el constructor para que siempre se muestre :)
        self.label_segundo_registro.configure(text=ultimo_alimento)
        total_calorias = self.calcular_calorias_totales() # lo mismo que el anterior pero para el total de calorías
        self.label_total_c_mostrar.configure(text=total_calorias)

    def add_widget_registro(self):
        self.bg_btn_agregar = ctk.CTkButton(self.sub, text='', bg_color=gris, state='disable', width=245, height=35, corner_radius=20)
        self.bg_btn_agregar.place(x=85, y=38)

        self.label_agregar = ctk.CTkLabel(self.sub, text="Seleccionar Alimento", text_color="white", font=("Arial", 20), bg_color=gris, width=200)
        self.label_agregar.place(x=95, y=40) # 85x

        self.combo_box = ctk.CTkComboBox(self.sub, corner_radius=20, fg_color=gris_label,
                                         values=self.cargar_alimentos(),
                                         border_width=0, button_color="#26656D",
                                         button_hover_color="white", text_color=negro_text,
                                         command=self.on_alimento_select)  # Añadimos el evento de selección
        self.combo_box.place(relx=0.1, rely=0.15, relwidth=0.3, relheight=0.05)

        self.combo_box.set("Seleccionar alimento")

        self.boton_ayuda = ctk.CTkButton(self.sub, text="i",
                                         command=self.mostrar_advertencia,
                                         corner_radius=15,
                                         width=30, height=30,
                                         font=("Times New Roman", 25, "italic"),
                                         text_color="white")
        self.boton_ayuda.place(relx=0.97, rely=0.04, anchor="ne")

        self.bg_btn_buscador = ctk.CTkButton(self.sub, text='', bg_color=gris, state='disable', width=245, height=35, corner_radius=20)
        self.bg_btn_buscador.place(x=85, y=145)

        self.label_buscar = ctk.CTkLabel(self.sub, text="Buscador de alimentos", text_color="white", bg_color=gris, font=("Arial", 20))
        self.label_buscar.place(x=95, y=147)

        self.entry_buscar = ctk.CTkEntry(self.sub, corner_radius=20, placeholder_text="Buscar alimento", 
                                         placeholder_text_color="black", border_width=0, fg_color="white", 
                                         text_color="black") 
        self.entry_buscar.place(relx=0.1, rely=0.35, relwidth=0.3) 
        self.entry_buscar.bind('<KeyRelease>', self.obtener_busqueda)

        self.coincidencias = Listbox(self.sub)
        self.coincidencias.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.055)
        self.coincidencias.bind('<<ListboxSelect>>', self.rellenar)

        self.alimentos_buscar = self.cargar_alimentos()
        self.match = []



        self.bg_btn_ultimo = ctk.CTkButton(self.sub, text='', bg_color=gris, state='disable', width=275, height=35, corner_radius=20, fg_color=oscuro)
        self.bg_btn_ultimo.place(x=410, y=38)

        self.label_registro = ctk.CTkLabel(self.sub, text="Último alimento registrado: ", text_color="white", 
                                           bg_color=gris, font=("Arial", 20))
        self.label_registro.place(x=420, y=40)

        self.label_segundo_registro = ctk.CTkLabel(self.sub, text="", text_color='white', bg_color=gris, font=("Arial", 20, 'bold'))
        self.label_segundo_registro.place(x=420, y=80)

        self.entry = ctk.CTkEntry(self.sub, corner_radius=20, placeholder_text="Ingrese cantidad consumida", 
                                  placeholder_text_color="black", border_width=0, fg_color="white", 
                                  text_color="black")

        self.boton_registrar = ctk.CTkButton(self.sub, text="Registrar", text_color="white", fg_color=verde_claro, corner_radius=20,
                                             hover_color=celeste_pero_oscuro, command=self.boton_mensanjes_insert, font=("Arial", 20))

        self.bg_btn_total = ctk.CTkButton(self.sub, text='', bg_color=gris, state='disable', width=275, height=35, corner_radius=20, fg_color=oscuro)
        self.bg_btn_total.place(x=410, y=145)

        self.label_total_calorias = ctk.CTkLabel(self.sub, text="Total calorías del día: ", text_color="white", 
                                                 bg_color=verde_oscuro, font=("Arial", 20))
        self.label_total_calorias.place(x=420, y=147)

        self.label_total_c_mostrar = ctk.CTkLabel(self.sub, text="", text_color='white',
                                                  bg_color=gris, font=("Arial", 20, 'bold'))
        self.label_total_c_mostrar.place(x=420, y=187)

    def on_alimento_select(self, selected_alimento):
        alimento_info = self.buscar_alimento_en_db(selected_alimento)

        if alimento_info:
            nombre, calorias_100g, calorias_porcion = alimento_info

            self.bg_btn_cal = ctk.CTkButton(self.sub, text='', bg_color=gris, state='disable', width=245, height=35, corner_radius=20)
            self.bg_btn_cal.place(x=85, y=250)

            self.label_calorias = ctk.CTkLabel(self.sub, text="Cantidad alimento", text_color="white", 
                                           font=("Arial", 20), bg_color=gris)

            if calorias_porcion is not None:
                self.label_calorias.configure(text=f"Cant. de porciones")
            else:
                self.label_calorias.configure(text=f"Cant. de alimento por gr")

            self.label_calorias.place(x=95, y=252)
            self.entry.place(relx=0.1, y=290, relwidth=0.3)
            self.boton_registrar.place(relx=0.1, rely=0.73, relwidth=0.3, relheight=0.085)

            self.bg_btn_hora = ctk.CTkButton(self.sub, text='', bg_color=gris, state='disable', width=275, height=35, corner_radius=20, fg_color=oscuro)
            self.bg_btn_hora.place(x=410, y=250)

            self.label_hora = ctk.CTkLabel(self.sub, text="Hora (HH:MM):", text_color="white", bg_color=verde_claro, font=("Arial", 20))
            self.label_hora.place(x=420, y=252)

            self.hour_var = ctk.IntVar(value=12)
            self.minute_var = ctk.IntVar(value=30)

            self.hour_slider = ctk.CTkSlider(self.sub, from_=0, to=23, variable=self.hour_var, command=self.update_time_label)
            self.hour_slider.place(relx=0.5, rely=0.55, relwidth=0.18)

            self.minute_slider = ctk.CTkSlider(self.sub, from_=0, to=59, variable=self.minute_var, command=self.update_time_label)
            self.minute_slider.place(relx=0.72, rely=0.55, relwidth=0.18)

            self.time_label = ctk.CTkLabel(self.sub, text="", text_color="white", font=("Arial", 16))
            self.time_label.place(relx=0.5, rely=0.60, relwidth=0.4, relheight=0.05)

            self.boton_hora_actual = ctk.CTkButton(self.sub, text="Hora Actual", command=self.set_current_time)
            self.boton_hora_actual.place(relx=0.5, rely=0.65, relwidth=0.4, relheight=0.05)

            self.update_time()


    def cargar_alimentos(self):
        conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
        cursor = conn.cursor()

        cursor.execute("SELECT nombre FROM alimento")
        alimentos = cursor.fetchall()

        lista_alimentos = [alimento[0] for alimento in alimentos if alimento[0] is not None]
        
        conn.close()
        return lista_alimentos

    def mostrar_advertencia(self):
        CTkMessagebox(title="Registrar Alimento", message="En esta pestaña, puedes registrar los alimentos consumidos durante el día y las calorías totales. Primero, debes añadir el alimento en la pestaña Agregar Alimento. Luego, podrás buscarlo con un buscador o ver todos los alimentos registrados.", icon='info', option_1="Ok")

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
        alimento_seleccionado = self.coincidencias.get(ctk.ACTIVE)
    
        self.entry_buscar.delete(0, ctk.END)
        self.entry_buscar.insert(0, alimento_seleccionado)

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
        self.actualizar_calorias_totales()
        self.boton_registrar_click()  

    def boton_registrar_click(self):
        alimento_seleccionado = self.combo_box.get()
        alimento_entry = self.entry_buscar.get().strip()
        
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
            nombre = alimento_info[0]
            self.label_registro.configure(text=f"Último alimento registrado:", font=("Arial", 20))
            self.label_segundo_registro.configure(text=f"{nombre}")
            self.combo_box.set("Seleccionar alimento")
            self.entry_buscar.delete(0, "end")
        else:
            CTkMessagebox(title="Alimento no encontrado", message="No se encontró el alimento en la base de datos.", icon='warning', option_1="Ok")
    
    def update_time_label(self, *args):
        hour = self.hour_var.get()
        minute = self.minute_var.get()
        self.time_label.configure(text=f"{hour:02}:{minute:02}")

    def set_current_time(self):
        now = datetime.now()
        self.hour_var.set(now.hour)
        self.minute_var.set(now.minute)
        self.update_time_label()
        
    def update_time(self):
        # Obtener la hora actual
        current_time = datetime.now().strftime("%H:%M")
        
        # Actualizar el texto de la etiqueta
        self.time_label.configure(text=current_time)
        
        self.sub.after(1000, self.update_time)


    # El codigo de Miguel adaptado bien pro
    def get_ultimo_insertado(self):
        conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
        cursor = conn.cursor()
        query = "SELECT nombre FROM consumo_diario WHERE id = (SELECT MAX(id) FROM consumo_diario);"
        cursor.execute(query)
        ultimo = cursor.fetchone()
        conn.close()

        if ultimo is None:
            return 'Agrega un alimento!'

        return ultimo[0]

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

        hora_actual = datetime.now().strftime('%H:%M')



        fecha_actual = datetime.now().strftime('%d-%m-%Y')

        alimento_seleccionado = self.combo_box.get()  
        alimento_entry = self.entry_buscar.get().strip()
        alimento = alimento_seleccionado if alimento_seleccionado != "Seleccionar alimento" else alimento_entry

        alimento_info = self.buscar_alimento_en_db(alimento)

        if alimento_info:
            nombre, calorias_100g, calorias_porcion = alimento_info

            try:

                cantidad = float(self.entry.get())
            except ValueError:
                CTkMessagebox(title="Error", message="Por favor, ingrese una cantidad válida.", icon='warning', option_1="Ok")
                return

            if calorias_porcion is not None:
                calorias_totales = calorias_porcion * cantidad
            else:  
                calorias_totales = (calorias_100g / 100) * cantidad

            cursor.execute('SELECT cantidad, total_cal FROM consumo_diario WHERE nombre = ? AND fecha = ?', (alimento, fecha_actual))
            resultado = cursor.fetchone()

            if resultado:
                cursor.execute(update_query, (cantidad, calorias_totales, alimento, fecha_actual))
            else:
                cursor.execute(insert_query, (alimento, fecha_actual, hora_actual, cantidad, calorias_totales))

            conn.commit()
            CTkMessagebox(title="Registro exitoso", message=f"Alimento {alimento} registrado con éxito.", icon='info', option_1="Ok")
        else:
            CTkMessagebox(title="Alimento no encontrado", message="No se encontró el alimento en la base de datos.", icon='warning', option_1="Ok")
    
        conn.close()
