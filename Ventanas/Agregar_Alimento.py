import customtkinter as ctk
from tkinter import Canvas
from Ventanas.Ventana_interfaz import New_ventana
from CTkMessagebox import CTkMessagebox


class Agregar_Alimento(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)
        self.add_widget_agregar()

    def add_widget_agregar(self):
    # Label "Buscador de alimentos"
        self.label_buscar = ctk.CTkLabel(self.sub, text="Añade alimento", text_color="black", bg_color="gray")
        self.label_buscar.place(relx=0.1, rely=0.2, relwidth=0.3, relheight=0.05)
        
        # Se crea el Entry "Buscar alimento"
        self.entry_buscar = ctk.CTkEntry(self.sub, corner_radius= 0, placeholder_text="Nombre del alimento", border_width=0)
        self.entry_buscar.place(relx=0.1, rely=0.25, relwidth=0.3, relheight=0.1) 

        # Label "Seleccione Cantidad Calorias"
        self.label_agregar = ctk.CTkLabel(self.sub, text="Seleccione Cantidad Calorias", text_color="black", bg_color="gray")
        self.label_agregar.place(relx=0.1, rely=0.45, relwidth=0.3, relheight=0.05)

        # ComboBox
        self.combo_box = ctk.CTkComboBox(self.sub, corner_radius=0, values=["","100gr", "Por porcion"],
                                        border_width=0)
        self.combo_box.place(relx=0.1, rely=0.5, relwidth=0.3, relheight=0.05)

        # Se crea el botón "Registrar" redondo
        self.boton_agregar = ctk.CTkButton(self.sub, text="+", text_color="black", fg_color="#f1faff",
                                  width=100, height=100, corner_radius=50,font=("Impact",50),
                                  command=self.boton_agregar_click)
        self.boton_agregar.place(relx=0.5, rely=0.3)

    def boton_agregar_click(self):  # Prueba de que funciona el botón "agregar alimento"
        CTkMessagebox(title="Alimento registrado", message="Se agrego el alimento correctamente") #Mensaje pro, funcionalidad basica
        print("Botón 'Registrar' clickeado")
