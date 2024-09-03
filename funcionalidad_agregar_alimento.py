import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
from Ventanas.Ventana_interfaz import New_ventana
import sqlite3 
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk


class New_ventana:
    def __init__(self, parent, color):
        self.parent = parent
        self.sub = ctk.CTkFrame(parent, fg_color=color, corner_radius=0)
        self.sub.pack(fill='both', expand=True)

class Registro_alimento(New_ventana):
    def __init__(self, parent, color):
        super().__init__(parent, color)
        self.add_widget_registro()

    def add_widget_registro(self):
        pass

class Agregar_alimento:
    def __init__(self, parent, color):
        self.parent = parent
        self.sub = ctk.CTkFrame(parent, fg_color=color)
        self.sub.pack(fill='both', expand=True)
        self.add_widget_agregar()

    def add_widget_agregar(self):
        self.nombre = ctk.CTkEntry(self.sub, height=50, width=300)
        self.nombre.place(x=50, y=60)

        self.formato = ctk.CTkOptionMenu(self.sub, height=50, width=300, values=['Por porción', 'Calorias en 100g'],
                                         command=self.cal_por)
        self.formato.place(x=50, y=130)

    def cal_por(self, valor):
        if valor == 'Por porción':
            self.mensage = ctk.CTkLabel(self.sub, text='Cuántas calorías tiene una porción?', font=('Arial', 20))
        elif valor == 'Calorias en 100g':
            self.mensage = ctk.CTkLabel(self.sub, text='¿Cuántas calorías hay en 100g?', font=('Arial', 20))
        self.mensage.place(x=50, y=200)

        self.calorias = ctk.CTkEntry(self.sub, height=50, width=300)
        self.calorias.place(x=50, y=250)

        self.insert = ctk.CTkButton(self.sub, text='+', height=150, width=150, corner_radius=100, fg_color='white',
                                    text_color='black', font=('arial', 30), hover_color='gray',
                                    command=self.new_alimento)
        self.insert.place(x=500, y=120)

    def new_alimento(self):
        try:
            nombre = self.nombre.get()
            seleccion = self.formato.get()
            calorias_texto = self.calorias.get()

            if not calorias_texto.isdigit():
                print('Calorías debe ser un número entero válido.')
                return

            cals = int(calorias_texto)

            self.sql_insert(nombre, cals, seleccion)
            print(f'Se insertó {nombre}, contiene {cals} calorías, el método será {seleccion}')
        except Exception as e:
            print(f'Error: {e}')

def sql_insert(self, nomb, n_cal, sel):
    try:
        conn = sqlite3.connect('alimentos.db')
        cursor = conn.cursor()

        if sel == 'Cuantas calorías hay en 100g':
            query = '''
            INSERT INTO alimentos (nombre, calorias_100g) VALUES (?, ?);
            '''
        else:
            query = '''
            INSERT INTO alimentos (nombre, calorias_porcion) VALUES (?, ?);
            '''

        cursor.execute(query, (nomb, n_cal))
        conn.commit()
        print('Alimento insertado con éxito!')

    except sqlite3.Error as error:
        print(f"Error al insertar en la base de datos: {error}")

    finally:
        if conn:
            conn.close()


class Grafico(New_ventana):
    def __init__(self, parent, color):
        super().__init__(parent, color)
        self.add_widget_grafico()

    def add_widget_grafico(self):
        pass

 
class Main(ctk.CTk):
    def __init__(self, size, title):
        super().__init__()
        self.title(title)
        self.geometry(size)
        self.resizable(False, False)
        self.add_paneles()
        self.add_widget_panel_superior()
        self.add_widget_panel_lateral()
        self.llamar_registro()

    def add_paneles(self):
        self.panel_superior = ctk.CTkFrame(self, fg_color='blue', height=100, corner_radius=0)
        self.panel_superior.pack(side=ctk.TOP, fill='both', expand=False)

        self.panel_lateral = ctk.CTkFrame(self, fg_color='red', width=150, corner_radius=0)
        self.panel_lateral.pack(side=ctk.LEFT, fill='both', expand=False)

        self.panel_principal = ctk.CTkFrame(self, fg_color='yellow', corner_radius=0)
        self.panel_principal.pack(side=ctk.RIGHT, fill='both', expand=True)

    def add_widget_panel_superior(self):
        self.titulo = ctk.CTkLabel(self.panel_superior, text='Contador de Calorías', font=('Arial', 20), pady=30)
        self.titulo.place(x=140, y=5)

        self.fecha = ctk.CTkLabel(self.panel_superior, text='Hoy es: ' + datetime.now().strftime('%d-%m-%Y'),
                                  font=('Arial', 20), pady=30)
        self.fecha.pack(side=ctk.RIGHT, padx=40)

        image = Image.open('uct-logo.28ec7a5d.png')
        ctk_image = ctk.CTkImage(image, size=(120, 60)) 

        self.logo = ctk.CTkLabel(self.panel_superior, image=ctk_image, text='')
        self.logo.place(x=10, y=5)
        self.logo.image = ctk_image

    def add_widget_panel_lateral(self):
        self.boton_1 = ctk.CTkButton(self.panel_lateral, text='Registra Alimento', font=('Arial', 16), fg_color='red',
                                     corner_radius=0, height=60, command=self.llamar_registro)
        self.boton_1.grid(row=0, column=0)

        self.boton_2 = ctk.CTkButton(self.panel_lateral, text='Agregar Alimento', font=('Arial', 16), fg_color='red',
                                     corner_radius=0, height=60, command=self.llamar_agregar)
        self.boton_2.grid(row=1, column=0)

        self.boton_3 = ctk.CTkButton(self.panel_lateral, text='Gráfico', font=('Arial', 16), fg_color='red',
                                     corner_radius=0, height=60, command=self.llamar_grafico)
        self.boton_3.grid(row=2, column=0)

    def llamar_registro(self):
        self.limpiar_panel(self.panel_principal)
        Registro_alimento(self.panel_principal, 'yellow')

    def llamar_agregar(self):
        self.limpiar_panel(self.panel_principal)
        Agregar_alimento(self.panel_principal, 'purple')

    def llamar_grafico(self):
        self.limpiar_panel(self.panel_principal)
        Grafico(self.panel_principal, 'orange')

    @staticmethod
    def limpiar_panel(panel):
        for win in panel.winfo_children():
            win.destroy()


root = Main(title='Calorie Tracker', size='1200x500')
root.mainloop()
