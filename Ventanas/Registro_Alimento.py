import customtkinter as ctk
from tkinter import Canvas
from Ventanas.Ventana_interfaz import New_ventana
from CTkMessagebox import CTkMessagebox


class Registro_Alimento(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)
        self.add_widget_registro()

    def add_widget_registro(self):
        # Rectangulo que acompaña el label "Agregar alimento"
        self.canvas_agregar = Canvas(self.sub, bg="gray", highlightthickness=0)
        self.canvas_agregar.place(relx=0.1, rely=0.3, relwidth=0.3, relheight=0.1)
        self.canvas_agregar.create_rectangle(2, 2, 298, 98, outline="", fill="gray") 

        # Label "Agregar alimento"
        self.label_agregar = ctk.CTkLabel(self.sub, text="Agregar alimento", text_color="white", bg_color="black")
        self.label_agregar.place(relx=0.1, rely=0.3, relwidth=0.3, relheight=0.05)

        # ComboBox
        self.combo_box = ctk.CTkComboBox(self.sub, corner_radius=0, fg_color="#183549", values=["Opción 1", "Opción 2", "Opción 3"],
                                         border_width=0, button_color="#26656D",
                                         button_hover_color="white", text_color="white")
        self.combo_box.place(relx=0.1, rely=0.35, relwidth=0.3, relheight=0.05)
        
        # Rectangulo que acompaña el Label "Buscador de alimentos"
        self.canvas_buscar = Canvas(self.sub, bg="gray", highlightthickness=0)  
        self.canvas_buscar.place(relx=0.1, rely=0.45, relwidth=0.3, relheight=0.1)
        self.canvas_buscar.create_rectangle(2, 2, 298, 98, outline="", fill="gray")  

        # Label "Buscador de alimentos"
        self.label_buscar = ctk.CTkLabel(self.sub, text="Buscador de alimentos", text_color="white", bg_color="black")
        self.label_buscar.place(relx=0.1, rely=0.45, relwidth=0.3, relheight=0.05)
        
        # Se crea el Entry "Buscar alimento"
        self.entry_buscar = ctk.CTkEntry(self.sub, corner_radius=0, placeholder_text="Buscar alimento", placeholder_text_color="black", border_width=0, fg_color="white") 
        self.entry_buscar.place(relx=0.1, rely=0.5, relwidth=0.3, relheight=0.1) 

        # Se crea el botón "Registrar"
        self.boton_agregar = ctk.CTkButton(self.sub, text="Registrar", text_color="white", fg_color="black",
                                           command=self.boton_agregar_click)
        self.boton_agregar.place(relx=0.1, rely=0.7, relwidth=0.3, relheight=0.05)
        
        
        # Registro
        
        self.canvas_agregar = Canvas(self.sub, bg="#1f2329", highlightthickness=0)
        self.canvas_agregar.place(relx=0.5, rely=0.3, relwidth=0.3, relheight=0.1)
        self.canvas_agregar.create_rectangle(2, 2, 298, 98, outline="", fill="#1f2329") 
        
        self.label_agregar = ctk.CTkLabel(self.sub, text="Último alimento registrado:" , text_color="white", bg_color="#183549")
        self.label_agregar.place(relx=0.5, rely=0.3, relwidth=0.3, relheight=0.05)

    def boton_agregar_click(self):  # Prueba de que funciona el botón "Registrar"
        CTkMessagebox(title="Alimento registrado", message="Se registraron x calorias creo", icon="info") #Mensaje pro, funcionalidad basica
        print("Botón 'Registrar' clickeado") 
