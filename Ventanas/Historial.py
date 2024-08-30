from Ventanas.Ventana_interfaz import New_ventana


class Historial(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)
        self.add_widget_historial()

    def add_widget_historial(self):
        pass
