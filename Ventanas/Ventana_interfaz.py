from abc import ABC
import customtkinter as ctk


class New_ventana(ABC):
    def __init__(self, parent, color):
        self.parent = parent
        self.sub = ctk.CTkFrame(parent, fg_color=color, corner_radius=0)
        self.sub.pack(fill='both', expand=True)
        self.usuario = self.obtener_usuario()
    
    def obtener_usuario(self):
        with open('usuario_actual.txt', 'r') as users:
                return users.readline()
