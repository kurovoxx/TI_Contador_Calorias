from Ventanas.Ventana_interfaz import New_ventana
from util.colores import *
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkinter import ttk, Scrollbar

class Alimentos(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)
        self.nombre = "admin_alimentos"
        self.widget_alimentos()
        self.mensage("Esta es la pestaña Admin alimentos, aqui podras ver todos los alimentos que has registrado, al igual que podras gestionar las calorias que tienen", "Admin Alimentos")

    def mostrar_advertencia(self):
        CTkMessagebox(title="Admin Alimentos", message="Esta es la pestaña Admin alimentos, aqui podras ver todos los alimentos que has registrado, al igual que podras gestionar las calorias que tienen", icon='info', option_1="Ok"),


    def widget_alimentos(self):
        self.treeview_alimentos = ctk.CTkFrame(self.sub, width=500)
        self.treeview_alimentos.pack(pady=60, padx=20, anchor="center")
        self.boton_ayuda = ctk.CTkButton(self.sub, text="i",
                                         command=self.mostrar_advertencia,
                                         corner_radius=15,
                                         width=30, height=30,
                                         font=("Times New Roman", 25, "italic"),
                                         text_color="white")
        self.boton_ayuda.place(relx=0.97, rely=0.04, anchor="ne")
        
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

    def editar_alimentos(self):
        print("presionado")
        pass
