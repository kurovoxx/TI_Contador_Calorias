import customtkinter as ctk
from tkinter import messagebox
from CTkMessagebox import CTkMessagebox  # Importa CTkMessagebox
from Ventanas.Ventana_interfaz import New_ventana
import sqlite3

class Configuracion(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)
        self.panel_principal = panel_principal 
        self.mostrar_messagebox()  # Mostrar Messagebox al abrir la pestaña
        self.add_widget_config()

    def mostrar_messagebox(self):
        """Muestra un Messagebox con información introductoria."""
        CTkMessagebox(
            title="Configuración",
            message="En esta sección puedes actualizar tu información personal como nombre, edad, peso y objetivo de calorías. "
                    "Recuerda guardar los cambios antes de salir.",
            icon="info",  # Tipo de ícono que deseas mostrar (info, warning, error)
            option_1="OK"  # Opción que ofrece el mensaje (puedes agregar más si es necesario)
        )

    def add_widget_config(self):
        # Título para el módulo configuración
        self.title_label = ctk.CTkLabel(self.sub, text="Actualizar información Usuario", text_color="white", font=("Arial", 27))
        self.title_label.pack(padx=20, pady=5, anchor="w")
        
        self.perfil_frame = ctk.CTkFrame(self.sub, width=300)
        self.perfil_frame.pack(padx=20, pady=10, anchor="w")

        self.edad_label = ctk.CTkLabel(self.perfil_frame, text="Edad:")
        self.edad_label.pack(anchor="w", padx=3, pady=(2, 0))
        
        self.edad_entry = ctk.CTkEntry(self.perfil_frame, placeholder_text="Introduce tu edad", width=250)
        self.edad_entry.pack(padx=3, pady=(0, 2))

        self.obj_calorias_label = ctk.CTkLabel(self.perfil_frame, text="Objetivo de Calorías:")
        self.obj_calorias_label.pack(anchor="w", padx=3, pady=(2, 0))
        
        self.obj_calorias_combobox = ctk.CTkComboBox(self.perfil_frame, values=["Pérdida de peso", "Mantenimiento", "Aumento de peso"], width=250)
        self.obj_calorias_combobox.pack(padx=3, pady=(0, 2))

        self.lvl_actividad_label = ctk.CTkLabel(self.perfil_frame, text="Nivel de Actividad:")
        self.lvl_actividad_label.pack(anchor="w", padx=3, pady=(2, 0))
        
        self.lvl_actividad_combobox = ctk.CTkComboBox(self.perfil_frame, values=["Sedentario", "Ligero", "Moderado", "Intenso"], width=250)
        self.lvl_actividad_combobox.pack(padx=3, pady=(0, 2))

        self.guardar_button = ctk.CTkButton(self.perfil_frame, text="Actualizar información", command=self.guardar, width=250)
        self.guardar_button.pack(pady=5)

        # Boton actualizar contra
        self.mostrar_contra_button = ctk.CTkButton(self.perfil_frame, text="Actualizar Contraseña", command=self.mostrar_formulario_contrasena, width=250)
        self.mostrar_contra_button.pack(pady=10)

    def mostrar_formulario_contrasena(self):
        # Crea ventana contra
        self.nueva_ventana = ctk.CTkToplevel(self.panel_principal)
        self.nueva_ventana.title("Actualizar Contraseña")
        self.nueva_ventana.geometry("400x300")  

        self.nombre_label = ctk.CTkLabel(self.nueva_ventana, text="Nombre de Usuario:")
        self.nombre_label.pack(anchor="w", padx=3, pady=(5, 0))

        self.nombre_entry = ctk.CTkEntry(self.nueva_ventana, placeholder_text="Introduce tu nombre de usuario", width=250)
        self.nombre_entry.pack(padx=3, pady=(0, 5))

        self.nueva_contra_label = ctk.CTkLabel(self.nueva_ventana, text="Nueva Contraseña:")
        self.nueva_contra_label.pack(anchor="w", padx=3, pady=(5, 0))

        self.nueva_contra_entry = ctk.CTkEntry(self.nueva_ventana, placeholder_text="Introduce la nueva contraseña", width=250, show='*')
        self.nueva_contra_entry.pack(padx=3, pady=(0, 5))

        self.actualizar_contra_button = ctk.CTkButton(self.nueva_ventana, text="Actualizar Contraseña", command=self.actualizar_contrasena, width=250)
        self.actualizar_contra_button.pack(pady=5)

    def guardar(self):
        try:
            with open("users/holi/datos_usuario.txt", "w") as archivo_n:
                edad = self.edad_entry.get()
                archivo_n.write(f'Edad: {edad}\n')

                objetivo_calorias = self.obj_calorias_combobox.get()
                archivo_n.write(f'Objetivo: {objetivo_calorias}\n')

                nivel_actividad = self.lvl_actividad_combobox.get()
                archivo_n.write(f'Nivel de actividad: {nivel_actividad}\n')

            messagebox.showinfo("Confirmación", "Los datos se actualizaron correctamente.")
            
        except FileNotFoundError:
            messagebox.showerror("Error", "Hubo un problema al guardar los datos.")

    def actualizar_contrasena(self):
        """Actualiza la contraseña en la base de datos."""
        nombre_usuario = self.nombre_entry.get()
        nueva_contra = self.nueva_contra_entry.get()

        if not nombre_usuario or not nueva_contra:
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")
            return

        try:
            conn = sqlite3.connect("./usuarios.db") 
            cursor = conn.cursor()

            cursor.execute("SELECT nombre FROM users WHERE nombre = ?", (nombre_usuario,))
            user = cursor.fetchone()

            if user:
                # Actualiza la contraseña del usuario :)
                cursor.execute("UPDATE users SET contra = ? WHERE nombre = ?", (nueva_contra, nombre_usuario))
                conn.commit()
                messagebox.showinfo("Confirmación", "La contraseña ha sido actualizada correctamente.")
            else:
                messagebox.showerror("Error", "El usuario no existe.")

            conn.close()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error en la base de datos: {e}")
