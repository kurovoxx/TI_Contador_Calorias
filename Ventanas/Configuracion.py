import customtkinter as ctk
from tkinter import messagebox
from CTkMessagebox import CTkMessagebox  # Importa CTkMessagebox
from Ventanas.Ventana_interfaz import New_ventana
import sqlite3

class Configuracion(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)
        self.nombre = 'configuracion'
        self.panel_principal = panel_principal 
        self.add_widget_config()
        self.mensage("Esta es la pestaña de configuracion, dentro podras configurar todo lo que es tu perfil como el objetivo de calorias y el nivel de actividad", "Configuracion")
        
    def add_widget_config(self):
        # Título para el módulo configuración
        self.title_label = ctk.CTkLabel(self.sub, text="Actualizar información Usuario", text_color="white", font=("Arial", 27))
        self.title_label.place(x=20, y=5)

        self.perfil_frame = ctk.CTkFrame(self.sub, width=230, height=400)
        self.perfil_frame.place(x=20, y=50)

        self.nombre_label = ctk.CTkLabel(self.perfil_frame, text="Nombre:")
        self.nombre_label.place(x=10, y=10)
        self.cargar_nombre_usuario()

        self.edad_label = ctk.CTkLabel(self.perfil_frame, text="Edad: 57")
        self.edad_label.place(x=10, y=50)

        self.genero_label = ctk.CTkLabel(self.perfil_frame, text="Genero:")
        self.genero_label.place(x=10, y=90)

        self.obj_calorias_label = ctk.CTkLabel(self.perfil_frame, text="Objetivo de Calorías:")
        self.obj_calorias_label.place(x=10, y=140)

        self.obj_calorias_combobox = ctk.CTkComboBox(self.perfil_frame, values=["1000 kcal", "1500 kcal", "2000 kcal"], width=120)

        self.obj_check_var = ctk.StringVar(value="off")
        self.obj_checkbox = ctk.CTkCheckBox(self.perfil_frame,text="" , command=self.Cambiar_a_combobox,
                                            variable=self.obj_check_var, onvalue="on", offvalue="off")
        self.obj_checkbox.place(x=150, y=140)

        self.lvl_actividad_label = ctk.CTkLabel(self.perfil_frame, text="Nivel de Actividad:")
        self.lvl_actividad_label.place(x=10, y=180)

        self.lvl_actividad_combobox = ctk.CTkComboBox(self.perfil_frame, values=["Sedentario", "Ligero", "Moderado", "Intenso"], width=130)

        self.lvl_check_var = ctk.StringVar(value="off")
        self.lvl_checkbox = ctk.CTkCheckBox(self.perfil_frame, text="",command=self.Cambiar_a_combobox_actividad,
                                            variable=self.lvl_check_var, onvalue="on", offvalue="off")
        self.lvl_checkbox.place(x=150, y=180)

        self.guardar_button = ctk.CTkButton(self.perfil_frame, text="Actualizar información", command=self.guardar, width=200)
        self.guardar_button.place(x=10, y=220)

        self.mostrar_contra_button = ctk.CTkButton(self.perfil_frame, text="Actualizar Contraseña", command=self.mostrar_formulario_contrasena, width=200)
        self.mostrar_contra_button.place(x=10, y=260)

    def Cambiar_a_combobox(self):
        if self.obj_check_var.get() == "on":
            self.obj_calorias_label.place_forget()
            self.obj_calorias_combobox.place(x=10, y=140)  
        else:
            self.obj_calorias_combobox.place_forget()
            self.obj_calorias_label.place(x=10, y=140) 

    def Cambiar_a_combobox_actividad(self):
        if self.lvl_check_var.get() == "on":
            self.lvl_actividad_label.place_forget()
            self.lvl_actividad_combobox.place(x=10, y=180)  
        else:
            self.lvl_actividad_combobox.place_forget()
            self.lvl_actividad_label.place(x=10, y=180) 
            
    def cargar_nombre_usuario(self):
        # obtiene el nombre del usuario actual, despues se muestra en el label de arribita
        nombre_usuario = self.usuario  
        self.nombre_label.configure(text=f"Nombre: {nombre_usuario}")

         
    def mostrar_formulario_contrasena(self):
        # Crea ventana contra
        self.nueva_ventana = ctk.CTkToplevel(self.panel_principal)
        self.nueva_ventana.title("Actualizar Contraseña")
        self.nueva_ventana.attributes('-topmost', True)
        self.nueva_ventana.geometry("400x300")  

        # muestra el nombre de usuario ingresado
        self.nombre_label = ctk.CTkLabel(self.nueva_ventana, text=f"Nombre de Usuario: {self.usuario}")
        self.nombre_label.pack(anchor="w", padx=3, pady=(5, 0))

        self.contra_anterior_label = ctk.CTkLabel(self.nueva_ventana, text="Contraseña Anterior:")
        self.contra_anterior_label.pack(anchor="w", padx=3, pady=(5, 0))
        self.contra_anterior_entry = ctk.CTkEntry(self.nueva_ventana, placeholder_text="Introduce tu contraseña anterior", width=250, show='*')
        self.contra_anterior_entry.pack(padx=3, pady=(0, 5))

        self.nueva_contra_label = ctk.CTkLabel(self.nueva_ventana, text="Nueva Contraseña:")
        self.nueva_contra_label.pack(anchor="w", padx=3, pady=(5, 0))
        self.nueva_contra_entry = ctk.CTkEntry(self.nueva_ventana, placeholder_text="Introduce la nueva contraseña", width=250, show='*')
        self.nueva_contra_entry.pack(padx=3, pady=(0, 5))

        self.confirmar_contra_label = ctk.CTkLabel(self.nueva_ventana, text="Confirmar Nueva Contraseña:")
        self.confirmar_contra_label.pack(anchor="w", padx=3, pady=(5, 0))
        self.confirmar_contra_entry = ctk.CTkEntry(self.nueva_ventana, placeholder_text="Confirma la nueva contraseña", width=250, show='*')
        self.confirmar_contra_entry.pack(padx=3, pady=(0, 5))

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
        nombre_usuario = self.usuario 
        contra_anterior = self.contra_anterior_entry.get()
        nueva_contra = self.nueva_contra_entry.get()
        confirmar_contra = self.confirmar_contra_entry.get()
        # valida la contra
        if not contra_anterior or not nueva_contra or not confirmar_contra:
            CTkMessagebox(title="Advertencia", message="Por favor, completa todos los campos.", icon="warning", option_1="Ok")
            return

        if nueva_contra != confirmar_contra:
            CTkMessagebox(title="Advertencia", message="La nueva contraseña y su confirmación no coinciden.", icon="warning", option_1="Ok")
            return

        try:
            conn = sqlite3.connect("./usuarios.db")
            cursor = conn.cursor()

            # consulta verificar contra
            cursor.execute("SELECT contra FROM users WHERE nombre = ?", (nombre_usuario,))
            user = cursor.fetchone()

            if user and user[0] == contra_anterior:
                # actualiza la contra si son iguales
                cursor.execute("UPDATE users SET contra = ? WHERE nombre = ?", (nueva_contra, nombre_usuario))
                conn.commit()
                CTkMessagebox(title="Confirmación", message="La contraseña ha sido actualizada correctamente.", icon="info", option_1="Ok")
            else:
                CTkMessagebox(title="Error", message="La contraseña anterior no es correcta.", icon="warning", option_1="Ok")

            conn.close()
        except sqlite3.Error as e:
            CTkMessagebox(title="Error", message=f"Error en la base de datos: {e}", icon="warning", option_1="Ok")

