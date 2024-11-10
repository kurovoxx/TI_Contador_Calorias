from abc import ABC
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox  
import sqlite3
from util.colores import *


class New_ventana(ABC):
    def __init__(self, parent, color, nombre):
        self.parent = parent
        self.nombre = nombre
        self.sub = ctk.CTkFrame(parent, fg_color=color, corner_radius=20, bg_color=azul_medio_oscuro)
        self.sub.pack(fill='both', expand=True)
        self.usuario = self.obtener_usuario()

    def obtener_usuario(self):
        """Obtiene el usuario actual desde un archivo de texto."""
        with open('usuario_actual.txt', 'r') as users:
            return users.readline().strip()

    def mensage(self, msg: str, title: str):
        """Muestra un CTkMessagebox con el mensaje y el título dados y actualiza la columna correspondiente en la base de datos."""

        try:
            conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
            cursor = conn.cursor()

            columna = self.nombre

            cursor.execute(f"PRAGMA table_info(mensajes)")
            columnas = [col[1] for col in cursor.fetchall()]

            if columna in columnas:

                cursor.execute(f"SELECT {columna} FROM mensajes")
                valor_actual = cursor.fetchone()

                if valor_actual and valor_actual[0] == 0:
                    return  

                CTkMessagebox(title=title, message=msg, icon='info', option_1="Ok")

                cursor.execute(f"UPDATE mensajes SET {columna} = 0")

                conn.commit()
                print(f"Columna '{columna}' actualizada correctamente.")
            else:
                print(f"Error: La columna '{columna}' no existe en la tabla 'mensajes'.")

        except sqlite3.Error as e:
            print(f"Error al actualizar la base de datos: {e}")
        finally:

            conn.close()
