from Ventanas.Ventana_interfaz import New_ventana


class Grafico(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)
        self.add_widget_grafico()

    def add_widget_grafico(self):
        pass
