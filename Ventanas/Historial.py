from Ventanas.Ventana_interfaz import New_ventana
from Ventanas.Agregar_Alimento import *
import customtkinter as ctk 
import datetime  as dt
import sqlite3
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
        self.conn = sqlite3.connect('alimentos.db')  # Conectar a la base de datos
        self.cursor = self.conn.cursor()
        
        
    def add_widget_historial(self):

        self.perfil_treeview = ctk.CTkFrame(self.sub, width=300) #se usa .sub envez de solamente el self
        self.perfil_treeview.pack(padx=20, pady=10,anchor="center") 

        # Widgets uno debajo del otro
        self.tree = ttk.Treeview(self.perfil_treeview, columns=("Alimento", "Calorias 100gr", "Calorias por porcion"), show="headings")
        self.tree.heading("Alimento", text="Alimento")
        self.tree.heading("Calorias 100gr", text="Calorias 100gr")
        self.tree.heading("Calorias por porcion", text="Calorias por porcion")
        self.tree.pack(anchor="w", padx=3, pady=3)

    def agregar_treeview(self):
        """Obtiene los datos de la base de datos y los inserta en el Treeview."""
        # Ejecutar una consulta para obtener todos los alimentos y sus calorías :(
        self.cursor.execute("SELECT nombre, calorias_100g, calorias_porcion FROM alimentos")
        registros = self.cursor.fetchall()  

        for registro in registros:
            self.tree.insert("", "end", values=registro)

    def __del__(self):
        """Cierra la conexión con la base de datos cuando se destruye la instancia."""
        self.conn.close()
