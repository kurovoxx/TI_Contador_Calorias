from Ventanas.Ventana_interfaz import New_ventana
from Ventanas.Agregar_Alimento import *
import customtkinter as ctk 
import datetime  as dt
import sqlite3
from tkcalendar import DateEntry
from tkinter import ttk # Esta cochinadaba daba error 
import re

class Historial(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)
        self.conectar_base_datos()
        self.add_widget_historial()
        self.agregar_treeview()

    def conectar_base_datos(self):
        """Conecta a la base de datos SQLite."""
        self.conn = sqlite3.connect('alimentos.db')
        self.cursor = self.conn.cursor()

    def add_widget_historial(self):
        self.canvas = tk.Canvas(self.sub, width=800, height=600)
        self.canvas.place(relx=0.5, rely=0.5, anchor="center")

        # Mostrar imagen con PIL
        self.img_historial = Image.open("./img/historial.png")
        self.img_historial = self.img_historial.resize((800, 600), Image.Resampling.LANCZOS)
        self.img_historial_tk = ImageTk.PhotoImage(self.img_historial)

        # Muestra imagen en el canvas
        self.canvas.create_image(0, 0, anchor="nw", image=self.img_historial_tk)
        
        """Añade los widgets a la ventana"""
        self.perfil_treeview = ctk.CTkFrame(self.sub, width=300)
        self.perfil_treeview.pack(padx=20, pady=10, anchor="center")

        self.date_label = ctk.CTkLabel(self.perfil_treeview, text="Selecciona una fecha:")
        self.date_label.pack(pady=5)

        self.date_entry = DateEntry(self.perfil_treeview, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='y-mm-dd')
        self.date_entry.pack(pady=5)

        self.filter_button = ctk.CTkButton(self.perfil_treeview, text="Filtrar por fecha", command=self.filtrar_por_fecha)
        self.filter_button.pack(pady=10)

        self.tree = ttk.Treeview(self.perfil_treeview, columns=("Alimento", "Cal/100gr/Porcion","Total Calorias","Hora"), show="headings")
        self.tree.heading("Alimento", text="Alimento")
        self.tree.heading("Cal/100gr/Porcion", text="Cal/100gr/Porcion")
        self.tree.heading("Total Calorias", text="Total Calorias")
        self.tree.heading("Hora",text="Hora")
        self.tree.pack(anchor="w", padx=3, pady=3)

    def agregar_treeview(self):
        self.cursor.execute("""
            SELECT nombre, 
                CASE 
                    WHEN calorias_porcion IS NOT NULL THEN 'Porción'
                    ELSE '100g'
                END AS tipo_caloria,
                CASE 
                    WHEN calorias_porcion IS NOT NULL THEN calorias_porcion
                    ELSE calorias_100g
                END AS total_calorias
            FROM alimentos
        """)
        
        tiempo = dt.datetime.now()
        registros = self.cursor.fetchall()
        
        # La fecha puesta es solo una referencia de como deberia verse, ya que no tiene relacion con la hora correcta ingresada
        for registro in registros:
            self.tree.insert("", "end", values=(registro[0], registro[1], registro[2],"{}:{}".format(tiempo.hour, tiempo.minute))) 
            
    def filtrar_por_fecha(self):
        """Filtra los alimentos por la fecha seleccionada."""
        fecha_seleccionada = self.date_entry.get_date()
        fecha_str = fecha_seleccionada.strftime('%Y-%m-%d')

        self.tree.delete(*self.tree.get_children())

        self.cursor.execute("SELECT nombre, calorias_100g, calorias_porcion FROM alimentos WHERE fecha_registro = ?", (fecha_str,))
        registros = self.cursor.fetchall()

        for registro in registros:
            self.tree.insert("", "end", values=registro)

    def __del__(self):
        """Cierra la conexión con la base de datos cuando se destruye la instancia."""
        self.conn.close()
