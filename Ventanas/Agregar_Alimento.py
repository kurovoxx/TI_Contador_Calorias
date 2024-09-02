import customtkinter as ctk
from tkinter import Canvas
from Ventanas.Ventana_interfaz import New_ventana
from CTkMessagebox import CTkMessagebox
import sqlite3  # Importamos el módulo sqlite3 para interactuar con la base de datos

class Agregar_Alimento(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)
        self.conectar_base_datos()  # Conectar a la base de datos al iniciar
        self.add_widget_agregar()

    def conectar_base_datos(self):
        """Conecta a la base de datos SQLite."""
        self.conn = sqlite3.connect('alimentos.db')  # Conectar a la base de datos
        self.cursor = self.conn.cursor()

    def add_widget_agregar(self):
        # Label "agregar" de alimentos
        self.label_agregar = ctk.CTkLabel(self.sub, text="Agregar Alimentos", text_color="white", bg_color="black")
        self.label_agregar.place(relx=0.1, rely=0.2, relwidth=0.3, relheight=0.05)
        
        # Se crea el Entry "agregar alimento"
        self.agregar = ctk.CTkEntry(self.sub, corner_radius=0, placeholder_text="Nombre del alimento",
                                    placeholder_text_color="white", border_width=0, fg_color="#183549",text_color="white")
        self.agregar.place(relx=0.1, rely=0.25, relwidth=0.3, relheight=0.1)   

        # ComboBox debajo del Entry
        self.combo_box = ctk.CTkComboBox(self.sub, corner_radius=0, fg_color="White",
                                         values=["", "100gr", "Por porción"], border_width=0, button_color="#26656D",
                                         button_hover_color="white", command=self.actualizar_label)
        self.combo_box.place(relx=0.1, rely=0.35, relwidth=0.3, relheight=0.05)

        # Label "Seleccione Cantidad Calorías"
        self.label_calorias = ctk.CTkLabel(self.sub, text="Calorías", text_color="White", fg_color="Black")
        self.label_calorias.place(relx=0.1, rely=0.45, relwidth=0.3, relheight=0.05)

        # Entry para cantidad de calorías, solo números
        vcmd = (self.sub.register(self.solo_numeros), "%S")
        self.entry_calorias = ctk.CTkEntry(self.sub, validate="key", validatecommand=vcmd,
                                           corner_radius=0, placeholder_text="0", placeholder_text_color="gray", 
                                           border_width=0, fg_color="#183549",text_color="white")
        self.entry_calorias.place(relx=0.1, rely=0.5, relwidth=0.3, relheight=0.05)

        # Se crea el botón "Registrar" redondo
        self.boton_agregar = ctk.CTkButton(self.sub, text="+", text_color="black", fg_color="#f1faff", width=100,
                                           height=100, corner_radius=50, font=("Impact", 50),
                                           command=self.boton_agregar_click)
        self.boton_agregar.place(relx=0.45, rely=0.3)

    def actualizar_label(self, *args):
        """Actualiza el texto del label de calorías según la selección del ComboBox."""
        seleccion = self.combo_box.get()
        if seleccion == "100gr":
            self.label_calorias.configure(text="Calorías por 100gr")
        elif seleccion == "Por porción":
            self.label_calorias.configure(text="Calorías por porción")
        else:
            self.label_calorias.configure(text="Calorías")

    def solo_numeros(self, c):
        """Valida que la entrada sea solo números."""
        return c.isdigit()

    def boton_agregar_click(self):
        """Funcionalidad del botón para agregar un alimento a la base de datos."""
        nombre_alimento = self.agregar.get().strip()
        calorias = self.entry_calorias.get().strip()
        seleccion = self.combo_box.get()

        if nombre_alimento == "" or calorias == "" or seleccion == "":
            CTkMessagebox(title="Error", message="Por favor, complete todos los campos.")
            return

        try:
            calorias = int(calorias)
        except ValueError:
            CTkMessagebox(title="Error", message="Por favor, ingrese un valor numérico válido para las calorías.")
            return

        # Verificar si el alimento ya existe en la base de datos
        self.cursor.execute("SELECT * FROM alimentos WHERE nombre = ?", (nombre_alimento,))
        resultado = self.cursor.fetchone()

        if resultado:
            CTkMessagebox(title="Error", message="El alimento ya existe en la base de datos.")
        else:
            if seleccion == "100gr":
                calorias_100g = calorias
                calorias_porcion = None
            else:  # Si es "Por porción"
                calorias_100g = None
                calorias_porcion = calorias

            # Insertar el alimento en la base de datos con las calorías correspondientes
            self.cursor.execute(
                "INSERT INTO alimentos (nombre, calorias_100g, calorias_porcion) VALUES (?, ?, ?)",
                (nombre_alimento, calorias_100g, calorias_porcion)
            )
            self.conn.commit()  # Guardar cambios en la base de datos
            CTkMessagebox(title="Alimento registrado", message=f"Se agregó {nombre_alimento} correctamente.")

        print(f"Botón 'Registrar' clickeado con alimento: {nombre_alimento}, calorías: {calorias}, selección: {seleccion}")

    def __del__(self):
        """Cierra la conexión con la base de datos cuando se destruye la instancia."""
        self.conn.close()
