from abc import ABC
import customtkinter as ctk


class New_ventana(ABC):
    def __init__(self, parent, color):
        self.parent = parent
        self.sub = ctk.CTkFrame(parent, fg_color=color, corner_radius=0)
        self.sub.pack(fill='both', expand=True)
