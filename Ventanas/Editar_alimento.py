import customtkinter as ctk
from CTkMessagebox import CTkMessagebox 
from datetime import datetime
import sqlite3
import re

class Editar(ctk.CTkToplevel):
    def __init__(self, parent, user, nombre,tipo_caloria, calorias, callbac=None):
        super().__init__(parent)
        self.parent = parent
        self.usuario = user
        self.callbac = callbac
        self.geometry('450x160')
        self.title('Editar Alimento')
        self.attributes('-topmost', True)
        self.resizable(False,False)
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True)
        self.originalN = nombre
        self.widget()

        self.name_entry.insert(0, nombre)
        self.calorias_combobox.set(tipo_caloria)
        self.calorias_entry.insert(0, calorias)
        
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

        self.button_save = ctk.CTkButton(self.main_frame,text="Guardar", command=self.guardar)
        self.button_save.place(y=120, x=160)
    
    def conexion(self):
        """Conecta a la base de datos SQLite."""
        self.conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
        self.cursor = self.conn.cursor()


    def guardar(self):
        Nnuevo = self.name_entry.get().strip()
        Ntipo_cal = self.calorias_combobox.get()
        Ncalorias = self.calorias_entry.get().strip()

        if not Nnuevo or not Ntipo_cal or not Ncalorias:
            CTkMessagebox(title="Advertencia", message="No puede dejar ningún campo vacío",
                        icon='warning', option_1="Ok")
            return

        if not re.match(r"^[a-zA-Z\s]+$", Nnuevo):
            CTkMessagebox(title="Error", message="El nombre del alimento solo debe contener letras",
                        icon='error', option_1="Ok")
            return

        try:
            Ncalorias = float(Ncalorias)
        except ValueError:
            CTkMessagebox(title="Error", message="Las calorías deben ser un número válido",
                        icon='error', option_1="Ok")
            return

        self.conexion()
        try:
            self.cursor.execute("""
                UPDATE alimento
                SET nombre = ?,
                    calorias_100gr = CASE 
                        WHEN ? = '100gr' THEN ?
                        ELSE NULL
                    END,
                    calorias_porcion = CASE 
                        WHEN ? = 'Porción' THEN ?
                        ELSE NULL
                    END
                WHERE nombre = ?
            """, (Nnuevo, Ntipo_cal, Ncalorias, Ntipo_cal, Ncalorias, self.originalN))

            self.conn.commit()
            
            if self.callbac:
                self.callbac()
            self.destroy()
            CTkMessagebox(title="Éxito", message="Alimento Actualizado", icon="check", option_1="Ok")

        except sqlite3.Error as e:
            CTkMessagebox(title="Error", message=f"Error en la base de datos: {str(e)}",
                        icon='error', option_1="Ok")
        finally:
            self.conn.close()


        
        