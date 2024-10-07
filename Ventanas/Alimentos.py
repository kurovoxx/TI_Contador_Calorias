from Ventanas.Ventana_interfaz import New_ventana
from util.colores import *
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

class Alimentos(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)
        self.widget_alimentos()

    

    def widget_alimentos(self):
        self.treeview_alimentos = ctk.CTkFrame(self.sub, width=500)
        self.treeview_alimentos.pack(pady=60, padx=20, anchor="center")
        
        self.label_food = ctk.CTkLabel(self.treeview_alimentos, text="Alimentos")
        self.label_food.pack(anchor="center")
        self.tree = ttk.Treeview(self.treeview_alimentos, columns=("Nombre", "Calorias por porcion", "calorias 100gr"), show="headings")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Calorias por porcion", text="Calorias por porcion")
        self.tree.heading("calorias 100gr", text="Calorias 100gr")
        self.tree.pack()
