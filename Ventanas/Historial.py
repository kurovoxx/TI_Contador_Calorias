from Ventanas.Ventana_interfaz import New_ventana
from Ventanas.Agregar_Alimento import *
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import datetime as dt
import sqlite3
from tkcalendar import DateEntry
from tkinter import ttk
from util.colores import *

class Historial(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)
        self.mostrar_messagebox()
        self.conectar_base_datos()
        self.add_widget_historial()
        self.agregar_treeview()

    def mostrar_messagebox(self):
        """Muestra un messagebox con una descripción de la funcionalidad de esta pestaña."""
        CTkMessagebox(
            title="Historial de Alimentos",
            message="En esta sección puedes ver el historial de los alimentos consumidos, filtrarlos por fecha y visualizar el total de calorías por porción o por 100 gramos.",
            icon="info",
            option_1="Ok"
        )

    def conectar_base_datos(self):
        """Conecta a la base de datos SQLite."""
        self.conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
        self.cursor = self.conn.cursor()

    def add_widget_historial(self):
        """Añade los widgets a la ventana"""
        self.perfil_treeview = ctk.CTkFrame(self.sub, width=300)
        self.perfil_treeview.pack(padx=20, pady=10, anchor="center")

        self.date_label = ctk.CTkLabel(self.perfil_treeview, text="Selecciona una fecha:")
        self.date_label.pack(pady=5)

        self.date_entry = DateEntry(self.perfil_treeview, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='y-mm-dd')
        self.date_entry.pack(pady=5)


        self.filter_button = ctk.CTkButton(self.perfil_treeview, text="Filtrar por fecha", command=self.filtrar_por_fecha)
        self.filter_button.pack(pady=10)

        self.tree = ttk.Treeview(self.perfil_treeview, columns=("Alimento", "Cal/100gr/Porcion", "Cantidad","Total Calorias","Fecha","Hora"), show="headings")
        self.tree.heading("Alimento", text="Alimento")
        self.tree.heading("Cal/100gr/Porcion", text="Cal/100gr/Porcion")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.heading("Total Calorias", text="Total Calorias")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.column("Alimento", width=150)
        self.tree.column("Cal/100gr/Porcion", width=120)
        self.tree.column("Cantidad", width=100)
        self.tree.column("Total Calorias", width=100)
        self.tree.column("Fecha", width=110)
        self.tree.column("Hora", width=95)
        self.tree.pack(anchor="w", padx=3, pady=3)
        
    def agregar_treeview(self):
        self.cursor.execute("""
            SELECT c.nombre,
                CASE 
                    WHEN a.calorias_porcion IS NOT NULL THEN 'Porción'
                    ELSE '100gr'
                END AS tipo_caloria,
                c.cantidad,
                c.total_cal,
                c.fecha,
                c.hora
            FROM consumo_diario c
            JOIN alimento a ON c.nombre = a.nombre
        """)

        registros = self.cursor.fetchall()

        for registro in registros:
            cantidad = f"{registro[2]} Gr" if registro[1] == '100gr' else str(registro[2])
            self.tree.insert("", "end", values=(registro[0], registro[1], cantidad, registro[3], registro[4], registro[5]))

    def filtrar_por_fecha(self):
        """Filtra los alimentos por la fecha seleccionada."""
        fecha_seleccionada = self.date_entry.get_date()
        fecha_str = fecha_seleccionada.strftime('%Y-%m-%d') 

        self.tree.delete(*self.tree.get_children())


        self.cursor.execute("""
            SELECT a.nombre,
                CASE 
                    WHEN a.calorias_porcion IS NOT NULL THEN 'Porción'
                    ELSE '100gr'
                END AS tipo_caloria,
                CASE 
                    WHEN a.calorias_porcion IS NOT NULL THEN a.calorias_porcion
                    ELSE a.calorias_100gr
                END AS total_calorias,
                TIME(c.fecha) AS hora
            FROM consumo_diario c
            JOIN alimento a ON c.nombre = a.nombre
            WHERE strftime('%Y-%m-%d', substr(c.fecha, 7, 4) || '-' || substr(c.fecha, 4, 2) || '-' || substr(c.fecha, 1, 2)) = ?
        """, (fecha_str,))
        
        registros = self.cursor.fetchall()


        print("Registros obtenidos:", registros)
        for registro in registros:
            self.tree.insert("", "end", values=registro)
    def __del__(self):
        """Cierra la conexión con la base de datos cuando se destruye la instancia."""
        self.conn.close()
