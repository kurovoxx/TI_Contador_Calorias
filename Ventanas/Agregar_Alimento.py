import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from Ventanas.Ventana_interfaz import New_ventana
import sqlite3 
import webbrowser
from util.colores import *



class Agregar_Alimento(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color, 'agregar_alimento')
        self.conectar_base_datos()
        self.add_widget_agregar()
        self.mensage("Esta es la pestaña de agregar alimento, para agregar un alimento debes insertar el nombre del alimento, las calorias por porcion o por 100 gramos", "Agregar Alimento")

    def mostrar_advertencia(self):
        CTkMessagebox(title="Agregar Alimento", message="Esta es la pestaña de agregar alimento, para agregar un alimento debes insertar el nombre del alimento, las calorias por porcion o por 100 gramos.", icon='info', option_1="Ok")

    def conectar_base_datos(self):
        self.conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
        self.cursor = self.conn.cursor()

    def add_widget_agregar(self):
        self.bg_btn_agregar = ctk.CTkButton(self.sub, text='', bg_color=gris, state='disable', width=245, 
                                            height=35, corner_radius=20, fg_color=azul_medio_oscuro)
        self.bg_btn_agregar.place(x=85, y=78)
        
        # Label "agregar" de alimentos
        self.label_agregar = ctk.CTkLabel(self.sub, font=("Arial", 20), text="Agregar Alimentos", text_color="white", fg_color=azul_medio_oscuro, bg_color=azul_medio_oscuro)
        self.label_agregar.place(x=95, y=80)

        self.boton_ayuda = ctk.CTkButton(self.sub, text="i",
                                         command=self.mostrar_advertencia,
                                         corner_radius=15,
                                         width=30, height=30,
                                         font=("Times New Roman", 25, "italic"),
                                         text_color="white")
        self.boton_ayuda.place(relx=0.97, rely=0.04, anchor="ne")

        # entry agregar alimento
        self.agregar = ctk.CTkEntry(self.sub, corner_radius=20, placeholder_text_color="black", bg_color=gris, 
                                    placeholder_text="Ingrese el nombre del alimento",
                                    border_width=0, fg_color=color_entry, text_color="black", width=245, height=35)
        self.agregar.place(x=85, y=120)

        self.bg_btn_calorias = ctk.CTkButton(self.sub, text='', bg_color=gris, state='disable', width=245, 
                                            height=35, corner_radius=20, fg_color=azul_medio_oscuro)
        self.bg_btn_calorias.place(x=410, y=78)

        # Label "Seleccione Cantidad Calorías"
        self.label_calorias = ctk.CTkLabel(self.sub, font=("Arial", 20), text="Porcion / 100gr", text_color="white", fg_color=azul_medio_oscuro, bg_color=azul_medio_oscuro)
        self.label_calorias.place(x=420, y=80)

        # Combobox
        self.combo_box = ctk.CTkComboBox(self.sub, corner_radius=20, values=["Por porción", "100gr"], border_width=0, button_hover_color="white", bg_color=gris,
                                         command=self.actualizar_label, text_color=negro_texto, fg_color=gris_label, button_color="#26656D", width=245, height=35)
        self.combo_box.place(x=410, y=120)

        self.api = ctk.CTkButton(self.sub, text='Buscar Calorías', command=self.redirigir_api, corner_radius=20, fg_color=verde_boton, hover_color=verde_oscuro,
                                 text_color='black', font=("Arial", 20))
        self.api.place(x=600, y=470)

    def actualizar_label(self, e):
        self.bg_btn_cant_calorias = ctk.CTkButton(self.sub, text='', bg_color=gris, state='disable', width=245, 
                                            height=35, corner_radius=20, fg_color=azul_medio_oscuro)
        self.bg_btn_cant_calorias.place(x=85, y=185)

        # Label "calorías"
        self.label_cant_calorias = ctk.CTkLabel(self.sub, font=("Arial", 20), text="Calorias", text_color="white", bg_color=azul_medio_oscuro)
        self.label_cant_calorias.place(x=95, y=187)

        # Entry calorias
        self.entry_calorias = ctk.CTkEntry(self.sub, corner_radius=20, placeholder_text_color="black",
                                           placeholder_text="Ingrese las calorías",
                                        border_width=0, fg_color=color_entry, text_color="black", width=245, height=35)
        self.entry_calorias.place(x=85, y=227)

        # Botón "Añadir Alimento"
        self.boton_agregar = ctk.CTkButton(self.sub, text="Añadir Alimento", font=("Arial", 20), text_color='black', 
                                           fg_color=verde_boton, hover_color=verde_oscuro, corner_radius=20,
                                           width=240, height=50, border_width=0, command=self.boton_agregar_click)
        self.boton_agregar.place(x=410, y=185)

        seleccion = self.combo_box.get()
        if seleccion == "100gr":
            self.label_calorias.configure(text="Calorías por 100gr")
        elif seleccion == "Por porción":
            self.label_calorias.configure(text="Calorías por porción")
        else:
            self.label_calorias.configure(text="Calorías")

    def boton_agregar_click(self):
        """Funcionalidad del botón para agregar un alimento a la base de datos."""
        nombre_alimento = self.agregar.get().strip()
        calorias = self.entry_calorias.get().strip()
        seleccion = self.combo_box.get()

        if nombre_alimento == "" or calorias == "" or seleccion == "" or calorias == '':
            CTkMessagebox(title="Advertencia", message="Complete todos los campos.",
                          icon='warning', option_1="Ok")
            return

        try:
            calorias = int(calorias)
        except ValueError:
            CTkMessagebox(title="Advertencia", message="Ingrese una cantidad válida de calorías.",
                          icon='warning', option_1="Ok")
            return

        # Verificar si el alimento ya existe en la base de datos
        self.cursor.execute("SELECT * FROM alimento WHERE nombre = ?", (nombre_alimento,))
        resultado = self.cursor.fetchone()

        if resultado:
            CTkMessagebox(title="Advertencia", message=f"'{nombre_alimento}' ya está registrado.",
                          icon='warning', option_1="Ok")
        else:
            if seleccion == "100gr":
                calorias_100g = calorias
                calorias_porcion = None
            else:
                calorias_100g = None
                calorias_porcion = calorias

            # Insertar el alimento en la base de datos con las calorías correspondientes
            self.cursor.execute(
                "INSERT INTO alimento (nombre, calorias_100gr, calorias_porcion) VALUES (?, ?, ?)",
                (nombre_alimento, calorias_100g, calorias_porcion)
            )
            self.conn.commit()
            CTkMessagebox(title="Exito", message=f"Se ha registrado '{nombre_alimento}' correctamente.",
                          icon='check', option_1="Ok")

    def redirigir_api(self):
        webbrowser.open("https://fitia.app/es/calorias-informacion-nutricional/")

    def __del__(self):
        """Cierra la conexión con la base de datos cuando se destruye la instancia."""
        self.conn.close()
