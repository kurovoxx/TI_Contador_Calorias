from Ventanas.Ventana_interfaz import New_ventana
from util.colores import *
import customtkinter as ctk

class Alimentos(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)