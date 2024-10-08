from Ventanas.Ventana_interfaz import New_ventana
from util.colores import *
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkinter import ttk, Scrollbar

class Alimentos(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)
        self.widget_alimentos()

    def widget_alimentos(self):
        self.treeview_alimentos = ctk.CTkFrame(self.sub, width=500)
        self.treeview_alimentos.pack(pady=60, padx=20, anchor="center")
        
        self.label_food = ctk.CTkLabel(self.treeview_alimentos, text="Alimentos")
        self.label_food.pack(anchor="center")

    
        self.tree = ttk.Treeview(self.treeview_alimentos, columns=("Nombre", "Porcion", "Calorias"), show="headings")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Porcion", text="Por porcion o 100gr")
        self.tree.heading("Calorias", text="Calorias")
        
 
        self.tree.column("Nombre", width=350)
        self.tree.column("Porcion", width=350)
        self.tree.column("Calorias", width=350)

        self.tree.pack(anchor="center")

        self.boton_change = ctk.CTkButton(self.sub, text="Editar Alimento", fg_color="#28242c", command=self.editar_alimentos(), height=50)
        self.boton_change.pack(pady=100,anchor="center")

    def editar_alimentos(self):
        print("presionado")
        pass