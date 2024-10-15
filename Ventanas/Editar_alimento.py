import customtkinter as ctk
from CTkMessagebox import ctkmessagebox
from datetime import datetime
import sqlite3

class Editar(ctk.CTkToplevel):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent
        self.usuario = user
        self.geometry('450x160')
        self.title('Editar Alimento')
        self.attributes('-topmost', True)
        self.resizable(False,False)
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True)
        self.widget()
        
    def widget(self):
        name_frame = ctk.CTkFrame(self.main_frame)
        name_frame.pack(fill="x", padx=10, pady=5)
        self.name_label = ctk.CTkLabel(name_frame, text="Nombre:", anchor="e", width=100)
        self.name_label.pack(side="left", padx=(0, 10))
        
        self.name_entry = ctk.CTkEntry(name_frame)
        self.name_entry.pack(side="left", expand=True, fill="x")
        tipo_calorias_frame = ctk.CTkFrame(self.main_frame)
        tipo_calorias_frame.pack(fill="x", padx=10, pady=5)
        
        self.tipo_calorias_label = ctk.CTkLabel(tipo_calorias_frame, text="Tipo de calorías:", anchor="e", width=100)
        self.tipo_calorias_label.pack(side="left", padx=(0, 10))
        Tcalorias = ["Porcion", "100gr"]
        self.calorias_combobox = ctk.CTkComboBox(tipo_calorias_frame, values=Tcalorias, state="readonly")
        self.calorias_combobox.pack(side="left", expand=True, fill="x")

        calorias_frame = ctk.CTkFrame(self.main_frame)
        calorias_frame.pack(fill="x", padx=10, pady=5)
        self.calorias_label = ctk.CTkLabel(calorias_frame, text="Calorías:", anchor="e", width=100)
        self.calorias_label.pack(side="left", padx=(0, 10))
        self.calorias_entry = ctk.CTkEntry(calorias_frame)
        self.calorias_entry.pack(side="left", expand=True, fill="x")

        self.button_save = ctk.CTkButton(self.main_frame,text="Guardar", command=self.guardar())
        self.button_save.place(y=120, x=160)
    
    def guardar(self):
        print("guardo")
        pass
        