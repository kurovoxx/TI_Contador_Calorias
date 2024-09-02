import customtkinter as ctk
from tkinter import Canvas, messagebox
from Ventanas.Ventana_interfaz import New_ventana


class Registro_Alimento(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)
        self.add_widget_registro()

    def add_widget_registro(self):
        # Rectángulo que acompaña el label "Agregar alimento"
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
        
        # Rectángulo que acompaña el Label "Buscador de alimentos"
        self.canvas_buscar = Canvas(self.sub, bg="gray", highlightthickness=0)  
        self.canvas_buscar.place(relx=0.1, rely=0.45, relwidth=0.3, relheight=0.1)
        self.canvas_buscar.create_rectangle(2, 2, 298, 98, outline="", fill="gray")  

        # Label "Buscador de alimentos"
        self.label_buscar = ctk.CTkLabel(self.sub, text="Buscador de alimentos", text_color="white", bg_color="black")
        self.label_buscar.place(relx=0.1, rely=0.45, relwidth=0.3, relheight=0.05)
        
        # Se crea el Entry "Buscar alimento"
        self.entry_buscar = ctk.CTkEntry(self.sub, corner_radius=0, placeholder_text="Buscar alimento", placeholder_text_color="black",
                                         border_width=0, fg_color="white", text_color="black") 
        self.entry_buscar.place(relx=0.1, rely=0.5, relwidth=0.3, relheight=0.1) 

        # Se crea el botón "Registrar"
        self.boton_agregar = ctk.CTkButton(self.sub, text="Registrar", text_color="white", fg_color="black",
                                           command=self.boton_agregar_click)
        self.boton_agregar.place(relx=0.1, rely=0.7, relwidth=0.3, relheight=0.05)
        
        # Registro
        self.canvas_registro = Canvas(self.sub, bg="#1f2329", highlightthickness=0)
        self.canvas_registro.place(relx=0.5, rely=0.3, relwidth=0.3, relheight=0.1)
        self.canvas_registro.create_rectangle(2, 2, 298, 98, outline="", fill="#1f2329") 
        
        self.label_registro = ctk.CTkLabel(self.sub, text="Último alimento registrado: ", text_color="white", bg_color="#183549")
        self.label_registro.place(relx=0.5, rely=0.3, relwidth=0.3, relheight=0.05)
        
        self.label_segundo_registro = ctk.CTkLabel(self.sub, text="", text_color="white", bg_color="#1f2329")
        self.label_segundo_registro.place(relx=0.5, rely=0.35, relwidth=0.3, relheight=0.05)


    def boton_agregar_click(self):  # Prueba de que funciona el botón "Registrar"
        alimento_registrado = self.entry_buscar.get()  # Obtiene el valor del Entry
        self.actualizar_registro(alimento_registrado)
        messagebox.showinfo("Alimento registrado", f"Se registró el alimento: {alimento_registrado}")
        print(f"Botón 'Registrar' clickeado. Alimento registrado: {alimento_registrado}")
    
    def actualizar_registro(self, alimento):
        coso = int(input("Ingrese la cantidad de calorías: "))
        # Actualiza el texto del label con el último alimento registrado
        self.label_registro.configure(text=f"Último alimento registrado: {alimento}")
        self.label_segundo_registro.configure(text=f"Calorías totales: {coso} kcal")
