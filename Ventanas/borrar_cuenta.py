import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import sqlite3
import os
import shutil

class BorrarCuenta(ctk.CTkToplevel):
    def __init__(self, parent, usuario, callback=None):
        super().__init__(parent)
        self.parent = parent
        self.usuario = usuario
        self.callback = callback
        
        self.title("Eliminar Cuenta")
        self.geometry("400x250")
        self.attributes('-topmost', True)
        self.resizable(False, False)
        
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.add_widgets()
    
    def add_widgets(self):
        # Etiqueta de advertencia
        advertencia_label = ctk.CTkLabel(
            self.main_frame, 
            text="Eliminar Cuenta",
            font=("Arial", 20, "bold")
        )
        advertencia_label.pack(pady=(20, 10))
        
        # Mensaje de confirmación
        mensaje_label = ctk.CTkLabel(
            self.main_frame, 
            text="Ingresa tu contraseña para confirmar la eliminación de la cuenta:",
            wraplength=350
        )
        mensaje_label.pack(pady=(10, 5))
        
        # Entry para contraseña
        self.contra_entry = ctk.CTkEntry(
            self.main_frame, 
            show="*", 
            width=250, 
            placeholder_text="Contraseña"
        )
        self.contra_entry.pack(pady=(5, 10))
        
        # Botón de eliminar
        eliminar_button = ctk.CTkButton(
            self.main_frame, 
            text="Eliminar Cuenta", 
            fg_color="red", 
            hover_color="darkred",
            command=self.confirmar_eliminacion
        )
        eliminar_button.pack(pady=(10, 5))
        
        # Botón de cancelar
        cancelar_button = ctk.CTkButton(
            self.main_frame, 
            text="Cancelar", 
            fg_color="gray", 
            hover_color="darkgray",
            command=self.destroy
        )
        cancelar_button.pack(pady=(5, 20))
    
    def confirmar_eliminacion(self):
        # Obtener contraseña ingresada
        contra_ingresada = self.contra_entry.get()
        
        try:
            # Conectar a la base de datos de usuarios
            conn = sqlite3.connect('usuarios.db')
            cursor = conn.cursor()

            # Verificar contraseña
            cursor.execute("SELECT contra FROM users WHERE nombre = ?", (self.usuario,))
            resultado = cursor.fetchone()

            if resultado and resultado[0] == contra_ingresada:
                # Cerrar conexión
                conn.close()

                # Eliminar directorio de usuario
                usuario_path = f'./users/{self.usuario}'
                if os.path.exists(usuario_path):
                    shutil.rmtree(usuario_path)

                # Eliminar usuario de la base de datos
                conn = sqlite3.connect('usuarios.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM users WHERE nombre = ?", (self.usuario,))
                conn.commit()
                conn.close()

                # Limpiar archivo de usuario actual
                with open('usuario_actual.txt', 'w') as f:
                    f.write('')

                # Mostrar mensaje de éxito
                CTkMessagebox(
                    title="Éxito", 
                    message="La cuenta se ha eliminado correctamente.", 
                    icon="check", 
                    option_1="OK"
                )
                
                # Cerrar ventana actual
                self.destroy()

                # Llamar al callback si está definido (por ejemplo, para volver a la pantalla de login)
                if self.callback:
                    self.callback()

            else:
                CTkMessagebox(
                    title="Error", 
                    message="La contraseña ingresada es incorrecta.", 
                    icon="warning", 
                    option_1="OK"
                )

        except Exception as e:
            CTkMessagebox(
                title="Error", 
                message=f"Error al eliminar la cuenta: {str(e)}", 
                icon="warning", 
                option_1="OK"
            )