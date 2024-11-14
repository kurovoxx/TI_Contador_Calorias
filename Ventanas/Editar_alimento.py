import customtkinter as ctk
from CTkMessagebox import CTkMessagebox 
from util.colores import *
import sqlite3
import re

class Editar(ctk.CTkToplevel):
    def __init__(self, parent, user, nombre, tipo_caloria, calorias, callbac=None):
        super().__init__(parent)
        self.parent = parent
        self.usuario = user
        self.callbac = callbac
        self.geometry('450x330')
        self.title('Editar Alimento')
        self.attributes('-topmost', True)
        self.resizable(False,False)
        self.main_frame = ctk.CTkFrame(self, fg_color=gris, corner_radius=0)
        self.main_frame.pack(fill="both", expand=True)
        self.originalN = nombre
        self.widget()

        self.name_entry.insert(0, nombre)
        self.calorias_combobox.set(tipo_caloria)
        self.calorias_entry.insert(0, calorias.split()[0] if isinstance(calorias, str) else calorias)
        
    def widget(self):
        self.name_label = ctk.CTkLabel(self.main_frame, text="Nombre", width=200, fg_color=azul_medio_oscuro, font=("Arial", 20))
        self.name_label.configure(corner_radius=20)
        self.name_label.pack(pady=(20, 4))
        
        self.name_entry = ctk.CTkEntry(self.main_frame, corner_radius=20, border_width=0, fg_color=color_entry, text_color="black", width=200)
        self.name_entry.pack(pady=(0, 10))
        
        self.tipo_calorias_label = ctk.CTkLabel(self.main_frame, text="Tipo de calorías", width=200, fg_color=azul_medio_oscuro, font=("Arial", 20))
        self.tipo_calorias_label.configure(corner_radius=20)
        self.tipo_calorias_label.pack(pady=(0, 4))

        Tcalorias = ["Porción", "100gr"]

        self.calorias_combobox = ctk.CTkComboBox(self.main_frame, values=Tcalorias, state="readonly", border_width=0, corner_radius=20, width=200,
                                                 fg_color=gris_label, button_color=verde_boton, button_hover_color=verde_oscuro, text_color=negro_texto)
        self.calorias_combobox.pack(pady=(0, 12))

        self.calorias_label = ctk.CTkLabel(self.main_frame, text="Calorías", width=200, fg_color=azul_medio_oscuro, font=("Arial", 20))
        self.calorias_label.configure(corner_radius=20)
        self.calorias_label.pack(pady=(0, 4))

        self.calorias_entry = ctk.CTkEntry(self.main_frame, corner_radius=20, border_width=0, fg_color=color_entry, text_color="black", width=200)
        self.calorias_entry.pack(pady=(0, 20))

        self.button_save = ctk.CTkButton(self.main_frame,text="Guardar", fg_color=verde_boton, border_width=0,
                                         hover_color=verde_oscuro, text_color=azul_medio_oscuro, command=self.guardar, corner_radius=20, width=200, font=("Arial", 18, 'bold'))
        self.button_save.pack(pady=10)
    
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