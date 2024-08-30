import customtkinter as ctk
from datetime import datetime
from abc import ABC
from PIL import Image, ImageTk


class New_ventana(ABC):
    def __init__(self, parent, color):
        self.parent = parent
        self.sub = ctk.CTkFrame(parent, fg_color=color, corner_radius=0)
        self.sub.pack(fill='both', expand=True)


class Registro_alimento(New_ventana):
    def __init__(self, parent, color):
        super().__init__(parent, color)
        self.add_widget_registro()

    def add_widget_registro(self):
        pass


class Agregar_alimento(New_ventana):
    def __init__(self, parent, color):
        super().__init__(parent, color)
        self.add_widget_agregar()

    def add_widget_agregar(self):
        pass


class Grafico(New_ventana):
    def __init__(self, parent, color):
        super().__init__(parent, color)
        self.add_widget_grafico()

    def add_widget_grafico(self):
        pass

 
class Main(ctk.CTk):
    def __init__(self, size, title):
        super().__init__()
        self.title(title)
        self.geometry(size)
        self.resizable(False, False)
        self.add_paneles()
        self.add_widget_panel_superior()
        self.add_widget_panel_lateral()
        self.llamar_registro()

    def add_paneles(self):
        self.panel_superior = ctk.CTkFrame(self, fg_color='blue', height=100, corner_radius=0)
        self.panel_superior.pack(side=ctk.TOP, fill='both', expand=False)

        self.panel_lateral = ctk.CTkFrame(self, fg_color='red', width=150, corner_radius=0)
        self.panel_lateral.pack(side=ctk.LEFT, fill='both', expand=False)

        self.panel_principal = ctk.CTkFrame(self, fg_color='yellow', corner_radius=0)
        self.panel_principal.pack(side=ctk.RIGHT, fill='both', expand=True)

    def add_widget_panel_superior(self):
        self.titulo = ctk.CTkLabel(self.panel_superior, text='Contador de Calorías', font=('Arial', 20), pady=30)
        self.titulo.place(x=140, y=5)

        self.fecha = ctk.CTkLabel(self.panel_superior, text='Hoy es: ' + datetime.now().strftime('%d-%m-%Y'),
                                  font=('Arial', 20), pady=30)
        self.fecha.pack(side=ctk.RIGHT, padx=40)

        image = Image.open('uct-logo.28ec7a5d.png')
        ctk_image = ctk.CTkImage(image, size=(120, 60))  # Ajusta el tamaño según sea necesario

        # Aplicar la imagen a un CTkLabel
        self.logo = ctk.CTkLabel(self.panel_superior, image=ctk_image, text='')
        self.logo.place(x=10, y=5)
        # Guardar una referencia de la imagen para evitar que se recolecte
        self.logo.image = ctk_image

    def add_widget_panel_lateral(self):
        self.boton_1 = ctk.CTkButton(self.panel_lateral, text='Registra Alimento', font=('Arial', 16), fg_color='red',
                                     corner_radius=0, height=60, command=self.llamar_registro)
        self.boton_1.grid(row=0, column=0)

        self.boton_2 = ctk.CTkButton(self.panel_lateral, text='Agregar Alimento', font=('Arial', 16), fg_color='red',
                                     corner_radius=0, height=60, command=self.llamar_agregar)
        self.boton_2.grid(row=1, column=0)

        self.boton_3 = ctk.CTkButton(self.panel_lateral, text='Gráfico', font=('Arial', 16), fg_color='red',
                                     corner_radius=0, height=60, command=self.llamar_grafico)
        self.boton_3.grid(row=2, column=0)

    def llamar_registro(self):
        self.limpiar_panel(self.panel_principal)
        Registro_alimento(self.panel_principal, 'yellow')

    def llamar_agregar(self):
        self.limpiar_panel(self.panel_principal)
        Agregar_alimento(self.panel_principal, 'purple')

    def llamar_grafico(self):
        self.limpiar_panel(self.panel_principal)
        Grafico(self.panel_principal, 'orange')

    @staticmethod
    def limpiar_panel(panel):
        for win in panel.winfo_children():
            win.destroy()


root = Main(title='Calorie Tracker', size='1200x500')
root.mainloop()
