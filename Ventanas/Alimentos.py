from Ventanas.Ventana_interfaz import New_ventana
from Ventanas.Editar_alimento import Editar
from util.colores import *
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkinter import ttk, Scrollbar
import sqlite3


class Alimentos(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)
        self.nombre = "admin_alimentos"
        self.widget_alimentos()
        self.conexion()
        self.datos()
        self.mensage("Esta es la pestaña Admin alimentos, aqui podras ver todos los alimentos que has registrado, al igual que podras gestionar las calorias que tienen", "Admin Alimentos")

    def conexion(self):
        """Conecta a la base de datos SQLite."""
        self.conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
        self.cursor = self.conn.cursor()

    def widget_alimentos(self):
        self.treeview_alimentos = ctk.CTkFrame(self.sub, width=500)
        self.treeview_alimentos.pack(pady=60, padx=20, anchor="center")
        
        self.label_food = ctk.CTkLabel(self.treeview_alimentos, text="Alimentos")
        self.label_food.pack(anchor="center")


        tree_frame = ttk.Frame(self.treeview_alimentos)
        tree_frame.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(tree_frame, columns=("Nombre", "Porcion", "Calorias"), show="headings")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Porcion", text="Por porcion o 100gr")
        self.tree.heading("Calorias", text="Calorias")
        
        self.tree.column("Nombre", width=300)
        self.tree.column("Porcion", width=300)
        self.tree.column("Calorias", width=300)

        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.boton_change = ctk.CTkButton(self.sub, text="Editar Alimento", fg_color="#28242c", command=self.editar_alimentos, height=60)
        self.boton_change.pack(pady=80,anchor="center")


    def datos(self):
        self.cursor.execute("""
            SELECT a.nombre,
                CASE 
                    WHEN a.calorias_porcion IS NOT NULL THEN 'Porción'
                    ELSE '100gr'
                END AS tipo_caloria,
                CASE
                    WHEN a.calorias_porcion IS NOT NULL THEN a.calorias_porcion
                    ELSE a.calorias_100gr
                END AS calorias
            FROM alimento a
        """)

        registros = self.cursor.fetchall()

        for registro in self.tree.get_children():
            self.tree.delete(registro)

        for registro in registros:
            self.tree.insert("", "end", values=(registro[0], registro[1], registro[2]))
            registros = self.cursor.fetchall()

        for registro in registros:
            cantidad = f"{registro[2]} Gr" if registro[1] == '100gr' else str(registro[2])
            self.tree.insert("", "end", values=(registro[0], registro[1], cantidad, registro[3], registro[4], registro[5]))
   
    def editar_alimentos(self):
        seleccion = self.tree.focus()
        if seleccion:
            valor = self.tree.item(seleccion, "values")
            if valor:
                nombre = valor[0]
                tipo_caloria = valor[1]
                calorias = valor[2]
                Editar(self.sub, self.usuario, nombre, tipo_caloria, calorias)