from Ventanas.Ventana_interfaz import New_ventana
from util.colores import *

class Salud(New_ventana):
     def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)
        self.add_widget_salud()

     def add_widget_salud(self):
        pass