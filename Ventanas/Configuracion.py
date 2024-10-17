import customtkinter as ctk
from tkinter import messagebox
from CTkMessagebox import CTkMessagebox
from Ventanas.Ventana_interfaz import New_ventana
import sqlite3
from datetime import datetime

class Configuracion(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)
        self.nombre = 'configuracion'
        self.panel_principal = panel_principal 
        self.ultimo_msj = None
        self.add_widget_config()
        self.recordar_actualizar_peso()
        self.mensage("Esta es la pestaña de configuracion, dentro podras configurar todo lo que es tu perfil como el objetivo de calorias y el nivel de actividad", "Configuracion")
        
    def mostrar_advertencia(self):
        CTkMessagebox(title="Configuracion", message="Esta es la pestaña de configuracion, dentro podras configurar todo lo que es tu perfil como el objetivo de calorias y el nivel de actividad.", icon='info', option_1="Ok"),

    def add_widget_config(self):
        self.boton_ayuda = ctk.CTkButton(self.sub, text="i",
                                         command=self.mostrar_advertencia,
                                         corner_radius=15,
                                         width=30, height=30,
                                         font=("Times New Roman", 25, "italic"),
                                         text_color="white")
        self.boton_ayuda.place(relx=0.97, rely=0.04, anchor="ne")
        
        edad, genero = self.cargar_datos_usuario()
        # Título para el módulo configuración
        self.title_label = ctk.CTkLabel(self.sub, text="Actualizar información Usuario", text_color="white", font=("Arial", 27))
        self.title_label.place(x=20, y=5)

        self.perfil_frame = ctk.CTkFrame(self.sub, width=230, height=400)
        self.perfil_frame.place(x=20, y=50)

        self.nombre_label = ctk.CTkLabel(self.perfil_frame, text="Nombre:")
        self.nombre_label.place(x=10, y=10)
        self.cargar_nombre_usuario()

        self.edad_label = ctk.CTkLabel(self.perfil_frame, text=f"Edad: {edad}")
        self.edad_label.place(x=10, y=50)

        self.genero_label = ctk.CTkLabel(self.perfil_frame, text=f"Género: {genero}")
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
        
        self.config_peso_button = ctk.CTkButton(self.perfil_frame, text="Configurar Recordatorio Peso", command=self.mostrar_formulario_recordatorio, width=200)
        self.config_peso_button.place(x=10, y=300)

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
        nombre_usuario = self.usuario  
        self.nombre_label.configure(text=f"Nombre: {nombre_usuario}")
        
    def cargar_datos_usuario(self):
        """Obtiene la edad, el género, la meta de calorías y el nivel de actividad del usuario desde la base de datos."""
        try:
            conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
            cursor = conn.cursor()

            cursor.execute("SELECT edad, genero, meta_cal, nivel_actividad FROM datos WHERE nombre = ?", (self.usuario,))
            user_data = cursor.fetchone()

            conn.close()

            if user_data:
                edad, genero, meta_cal, nivel_actividad = user_data
                self.obj_calorias_original = meta_cal
                self.lvl_actividad_original = nivel_actividad
                return edad, genero
            else:
                return "N/A", "N/A"

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al acceder a la base de datos: {e}")
            return "N/A", "N/A"
        
    def mostrar_formulario_recordatorio(self):
        self.ventana_recordatorio = ctk.CTkToplevel(self.panel_principal)
        self.ventana_recordatorio.title("Configurar Recordatorio de Peso")
        self.ventana_recordatorio.geometry("400x350")
        self.ventana_recordatorio.attributes('-topmost', True)

        ctk.CTkLabel(self.ventana_recordatorio, text="Frecuencia de Recordatorio:").pack(anchor="w", padx=3, pady=10)

        # ComboBox para seleccionar la frecuencia
        self.tiempo_recordatorio_combobox = ctk.CTkComboBox(
            self.ventana_recordatorio,
            values=["1 día", "3 días", "5 días", "1 semana", "1 mes"],
            width=200
        )
        self.tiempo_recordatorio_combobox.pack(padx=3, pady=5)

        # CheckBox para activar o desactivar el recordatorio
        self.activar_recordatorio_var = ctk.StringVar(value="on")
        self.activar_recordatorio_checkbox = ctk.CTkCheckBox(
            self.ventana_recordatorio, text="Activar Recordatorio", 
            variable=self.activar_recordatorio_var, onvalue="on", offvalue="off"
        )
        self.activar_recordatorio_checkbox.pack(anchor="w", padx=3, pady=5)

        # Botón para guardar la configuración
        ctk.CTkButton(
            self.ventana_recordatorio, text="Guardar Configuración", 
            command=self.guardar_configuracion_recordatorio
        ).pack(pady=10)

        self.cargar_configuracion_recordatorio()
            
    def cargar_configuracion_recordatorio(self):
        try:
            conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
            cursor = conn.cursor()

            cursor.execute("SELECT recordatorio, cantidad_dias FROM datos WHERE nombre = ?", (self.usuario,))
            config = cursor.fetchone()
            conn.close()

            if config:
                estado, frecuencia = config
                self.activar_recordatorio_var.set(estado)
                self.tiempo_recordatorio_combobox.set(frecuencia)
            else:
                self.activar_recordatorio_var.set("off")
                self.tiempo_recordatorio_combobox.set("1 día")
        except sqlite3.Error as e:
            CTkMessagebox(title="Error", message=f"Error al cargar configuración: {e}", icon="error", option_1="OK")

    def guardar_configuracion_recordatorio(self):
        estado = self.activar_recordatorio_var.get()
        frecuencia = self.tiempo_recordatorio_combobox.get()

        try:
            conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE datos 
                SET recordatorio = ?, cantidad_dias = ? 
                WHERE nombre = ?
            """, (estado, frecuencia, self.usuario))

            conn.commit()
            conn.close()

            CTkMessagebox(title="Confirmación", message="Configuración guardada correctamente.", icon="info", option_1="OK")
            self.ventana_recordatorio.destroy()
        except sqlite3.Error as e:
            CTkMessagebox(title="Error", message=f"Error al guardar configuración: {e}", icon="error", option_1="OK")

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
        """Actualiza los datos de la base de datos con la nueva meta de calorías y nivel de actividad."""
        try:
            # Obtener los valores seleccionados
            if self.obj_check_var.get() == "on":
                objetivo_calorias = self.obj_calorias_combobox.get()
            else:
                objetivo_calorias = self.obj_calorias_original
        
            if self.lvl_check_var.get() == "on":
                nivel_actividad = self.lvl_actividad_combobox.get()
            else:
                nivel_actividad = self.lvl_actividad_original

            # Comparar con los valores originales
            if objetivo_calorias == self.obj_calorias_original and nivel_actividad == self.lvl_actividad_original:
                CTkMessagebox(
                    title="Sin Cambios",
                    message="No se han realizado cambios en la información.",
                    icon="info",
                    option_1="OK"
                )
            else:
                # Conexión a la base de datos
                conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
                cursor = conn.cursor()

                # Actualizar solo si hay cambios
                cursor.execute("""
                    UPDATE datos
                    SET meta_cal = ?, nivel_actividad = ?
                    WHERE nombre = ?
                """, (objetivo_calorias, nivel_actividad, self.usuario))

                # Confirmar los cambios
                conn.commit()

                # Mostrar mensaje de confirmación
                CTkMessagebox(
                    title="Confirmación",
                    message="Los datos se actualizaron correctamente.",
                    icon="info",
                    option_1="OK"
                )
                conn.close()

        except sqlite3.Error as e:
            CTkMessagebox(
                title="Error",
                message=f"Hubo un problema al guardar los datos en la base de datos: {e}",
                icon="warning",
                option_1="OK"
            )

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
            
    def mostrar_mensaje_recordatorio(self):
        CTkMessagebox(
            title="Recordatorio", 
            message="No has registrado tu peso según la frecuencia establecida. Por favor, actualiza tu peso.", 
            icon="warning", option_1="OK"
        )
            
    def recordar_actualizar_peso(self):
        try:
            conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
            cursor = conn.cursor()

            cursor.execute("SELECT recordatorio, cantidad_dias FROM datos WHERE nombre = ?", (self.usuario,))
            config = cursor.fetchone()

            if config:
                estado, frecuencia = config
                if estado == "on":  
                    frecuencia_dias = int(frecuencia.split()[0])

                    cursor.execute("SELECT fecha FROM peso ORDER BY fecha DESC LIMIT 1")
                    ultimo_registro = cursor.fetchone()

                    if ultimo_registro is not None and ultimo_registro[0]:
                        ultima_fecha = datetime.strptime(ultimo_registro[0], '%d-%m-%Y')
                        dias_diferencia = (datetime.now() - ultima_fecha).days

                        if dias_diferencia >= frecuencia_dias:
                            self.mostrar_mensaje_recordatorio_unavez(cursor)
                    else:
                        self.mostrar_mensaje_recordatorio_unavez(cursor)

            conn.commit()
            conn.close()

        except sqlite3.Error as e:
            CTkMessagebox(title="Error", message=f"Error al acceder a la base de datos: {e}", icon="info", option_1="OK")
        except Exception as e:
            CTkMessagebox(title="Error", message=f"Error inesperado: {e}", icon="info", option_1="OK")

    def mostrar_mensaje_recordatorio_unavez(self, cursor):
        fecha_hoy = datetime.now().date()

        if self.ultimo_msj != fecha_hoy:
            CTkMessagebox(
                title="Recordatorio",
                message="No has registrado tu peso según la frecuencia establecida. Por favor, actualiza tu peso.",
                icon="warning", option_1="OK"
            )
            self.ultimo_msj = fecha_hoy  

            cursor.execute("""
                UPDATE datos 
                SET recordatorio = 'off' 
                WHERE nombre = ?
            """, (self.usuario,))
