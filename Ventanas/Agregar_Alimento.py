import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from Ventanas.Ventana_interfaz import New_ventana
import sqlite3 
import webbrowser
from util.colores import *



class Agregar_Alimento(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)
        self.nombre = 'agregar_alimento'
        self.conectar_base_datos()
        self.add_widget_agregar()
        self.mensage("Esta es la pestaña de agregar alimento, para agregar un alimento debes insertar el nombre del alimento, las calorias por porcion o por 100 gramos", "Agregar Alimento")

    def mostrar_advertencia(self):
        CTkMessagebox(title="Agregar Alimento", message="Esta es la pestaña de agregar alimento, para agregar un alimento debes insertar el nombre del alimento, las calorias por porcion o por 100 gramos.", icon='info', option_1="Ok")

    def conectar_base_datos(self):
        self.conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
        self.cursor = self.conn.cursor()

    def add_widget_agregar(self):
        # Label "agregar" de alimentos
        self.label_agregar = ctk.CTkLabel(self.sub, font=("Arial", 20), text="Agregar Alimentos", text_color="white", bg_color=azul_medio_oscuro)
        self.label_agregar.place(relx=0.1, rely=0.15, relwidth=0.3, relheight=0.05)

        self.boton_ayuda = ctk.CTkButton(self.sub, text="i",
                                         command=self.mostrar_advertencia,
                                         corner_radius=15,
                                         width=30, height=30,
                                         font=("Times New Roman", 25, "italic"),
                                         text_color="white")
        self.boton_ayuda.place(relx=0.97, rely=0.04, anchor="ne")

        # entry agregar alimento
        self.agregar = ctk.CTkEntry(self.sub, corner_radius=0, placeholder_text_color="black", 
                                    placeholder_text="Ingrese el nombre del alimento",
                                    border_width=0, fg_color=color_entry, text_color="black")
        self.agregar.place(relx=0.1, rely=0.2, relwidth=0.3, relheight=0.05)

        # Label "Seleccione Cantidad Calorías"
        self.label_calorias = ctk.CTkLabel(self.sub,font=("Arial", 20), text="Porcion / 100gr", text_color="White", fg_color=azul_medio_oscuro)
        self.label_calorias.place(relx=0.5, rely=0.15, relwidth=0.3, relheight=0.05)  # Ajustar rely

        # Combobox
        self.combo_box = ctk.CTkComboBox(self.sub, corner_radius=0, values=["Por porción", "100gr"], border_width=0, button_hover_color="white",
                                         command=self.actualizar_label, text_color=negro_texto, fg_color=gris_label, button_color="#26656D")
        self.combo_box.place(relx=0.5, rely=0.2, relwidth=0.3, relheight=0.05)

        self.api = ctk.CTkButton(self.sub, text='Buscar Calorías', command=self.redirigir_api)
        self.api.place(x=500, y=500)

    def actualizar_label(self, e):
        # Label "calorías"
        self.label_agregar = ctk.CTkLabel(self.sub, font=("Arial", 20), text="Calorias", text_color="white", bg_color=azul_medio_oscuro)
        self.label_agregar.place(relx=0.1, rely=0.383, relwidth=0.3, relheight=0.05)

        # Entry calorias
        self.entry_calorias = ctk.CTkEntry(self.sub, corner_radius=0, placeholder_text_color="black",
                                           placeholder_text="Ingrese las calorías",
                                        border_width=0, fg_color=color_entry, text_color="black")
        self.entry_calorias.place(relx=0.1, rely=0.434, relwidth=0.3, relheight=0.05)

        # Botón "Añadir Alimento"
        self.boton_agregar = ctk.CTkButton(self.sub, text="Añadir Alimento", font=("Arial", 20), text_color='black', 
                                           fg_color=verde_boton, hover_color=verde_oscuro, 
                                           width=240, height=50, border_width=0, command=self.boton_agregar_click)
        self.boton_agregar.place(relx=0.5, rely=0.39)

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
        webbrowser.open("https://www.xvideos.com/video.ultiehbbf6b/hermanastros_cachondos_masturbandose_con_porno_gay_y_luego_follando")

    def __del__(self):
        """Cierra la conexión con la base de datos cuando se destruye la instancia."""
        self.conn.close()
