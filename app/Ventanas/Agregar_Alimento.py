from Ventanas.Ventana_interfaz import New_ventana


class Agregar_Alimento(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)
        self.add_widget_agregar()

    def add_widget_agregar(self):
        pass
