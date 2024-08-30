import customtkinter as ctk
from tkinter import Canvas
from Ventanas.Ventana_interfaz import New_ventana

class Registro_Alimento(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)
        self.add_widget_registro()

    def add_widget_registro(self):
        
        # Se usa canvas para el rectangulo que acompaña el label "Agregar alimento"
        self.canvas_agregar = Canvas(self.sub, bg="gray", highlightthickness=0)  
        self.canvas_agregar.place(relx=0.1, rely=0.3, relwidth=0.3, relheight=0.1)
        self.canvas_agregar.create_rectangle(2, 2, 298, 98, outline="", fill="gray") 

        # Label "Agregar alimento"
        self.label_agregar = ctk.CTkLabel(self.sub, text="Agregar alimento", text_color="black", bg_color="gray")
        self.label_agregar.place(relx=0.1, rely=0.3, relwidth=0.3, relheight=0.05)

        # Se crea el ComboBox
        self.combo_box = ctk.CTkComboBox(self.sub, corner_radius= 0, values=["Opción 1", "Opción 2", "Opción 3"]) 
        self.combo_box.place(relx=0.1, rely=0.35, relwidth=0.3, relheight=0.05)
        
        # Se usa canvas para el rectangulo que acompaña el Label "Buscador de alimentos"
        self.canvas_buscar = Canvas(self.sub, bg="gray", highlightthickness=0)  
        self.canvas_buscar.place(relx=0.1, rely=0.45, relwidth=0.3, relheight=0.1)
        self.canvas_buscar.create_rectangle(2, 2, 298, 98, outline="", fill="gray")  

        # Label "Buscador de alimentos"
        self.label_buscar = ctk.CTkLabel(self.sub, text="Buscador de alimentos", text_color="black", bg_color="gray", corner_radius = 0)
        self.label_buscar.place(relx=0.1, rely=0.45, relwidth=0.3, relheight=0.05)
        
        # Se crea el Entry "Buscar alimento"
        self.entry_buscar = ctk.CTkEntry(self.sub, placeholder_text="Buscar alimento")
        self.entry_buscar.place(relx=0.1, rely=0.5, relwidth=0.3, relheight=0.1) 

        # Se crea el botón "Registrar"
        self.boton_agregar = ctk.CTkButton(self.sub, text="Registrar", text_color="black", fg_color="#f1faff", command=self.boton_agregar_click)
        self.boton_agregar.place(relx=0.1, rely=0.7, relwidth=0.3, relheight=0.05)

    def boton_agregar_click(self): # Prueba de que funciona el botón "Registrar"
        print("Botón 'Registrar' clickeado")
