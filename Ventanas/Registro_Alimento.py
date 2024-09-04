import customtkinter as ctk
import sqlite3
from tkinter import messagebox
from Ventanas.Ventana_interfaz import New_ventana

class Registro_Alimento(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)
        self.add_widget_registro()
        self.cargar_alimentos()

    def add_widget_registro(self):
        # Label "Agregar alimento"
        self.label_agregar = ctk.CTkLabel(self.sub, text="Agregar alimento", text_color="white", bg_color="black")
        self.label_agregar.place(relx=0.1, rely=0.3, relwidth=0.3, relheight=0.05)

        # ComboBox dinámico, será llenado desde la base de datos
        self.combo_box = ctk.CTkComboBox(self.sub, corner_radius=0, fg_color="#183549",
                                         values=[],  # Inicialmente vacío, lo llenaremos después
                                         border_width=0, button_color="#26656D",
                                         button_hover_color="white", text_color="white")
        self.combo_box.place(relx=0.1, rely=0.35, relwidth=0.3, relheight=0.05)

        # Mensaje "predeterminado" para el combobox
        self.combo_box.set("Seleccionar alimento")  

        # Label "Buscador de alimentos"
        self.label_buscar = ctk.CTkLabel(self.sub, text="Buscador de alimentos", text_color="white", bg_color="black")
        self.label_buscar.place(relx=0.1, rely=0.45, relwidth=0.3, relheight=0.05)
        
        # Entry "Buscar alimento" que también estará vinculado a la búsqueda
        self.entry_buscar = ctk.CTkEntry(self.sub, corner_radius=0, placeholder_text="Buscar alimento", 
                                         placeholder_text_color="black", border_width=0, fg_color="white", 
                                         text_color="black") 
        self.entry_buscar.place(relx=0.1, rely=0.5, relwidth=0.3, relheight=0.1) 

        # Botón "Registrar"
        self.boton_buscar = ctk.CTkButton(self.sub, text="Registrar", text_color="white", fg_color="black", 
                                          hover_color="#007bff", command=self.boton_registrar_click)
        self.boton_buscar.place(relx=0.1, rely=0.65, relwidth=0.3, relheight=0.05)

        # Registro        
        self.label_registro = ctk.CTkLabel(self.sub, text="Último alimento registrado: ", text_color="white", 
                                           bg_color="#183549")
        self.label_registro.place(relx=0.5, rely=0.3, relwidth=0.3, relheight=0.05)
        
        self.label_segundo_registro = ctk.CTkLabel(self.sub, text="", text_color="white", bg_color="#1f2329")
        self.label_segundo_registro.place(relx=0.5, relwidth=0.3, relheight=0.05, rely=0.35)

    def cargar_alimentos(self):
        conn = sqlite3.connect('alimentos.db')
        cursor = conn.cursor()

        cursor.execute("SELECT nombre FROM alimentos")
        alimentos = cursor.fetchall()

        # Cargar los alimentos en el ComboBox
        lista_alimentos = [alimento[0] for alimento in alimentos]
        self.combo_box.configure(values=lista_alimentos)
        
        conn.close()

    def boton_registrar_click(self):
        # Obtener el alimento desde el ComboBox o desde el Entry
        alimento_seleccionado = self.combo_box.get()
        alimento_entry = self.entry_buscar.get().strip()

        if alimento_seleccionado != "Seleccionar alimento":  # Si se seleccionó un alimento en el ComboBox
            alimento = alimento_seleccionado
        elif alimento_entry:  # Si no hay selección en el ComboBox pero hay texto en el Entry
            alimento = alimento_entry
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un alimento o ingresa uno válido.")
            return
        
        # Consultar el alimento en la base de datos
        alimento_info = self.buscar_alimento_en_db(alimento)
        
        if alimento_info:  # Si el alimento fue encontrado
            nombre, calorias_100g, calorias_porcion = alimento_info
            
            # Mostrar el nombre del alimento
            self.label_registro.configure(text=f"Último alimento registrado: {nombre}")
            
            # Mostrar las calorías en porción o por 100g
            if calorias_porcion:
                self.label_segundo_registro.configure(text=f"Calorías totales: {calorias_porcion} por porción")
            else:
                self.label_segundo_registro.configure(text=f"Calorías totales: {calorias_100g} por 100g")
            
            messagebox.showinfo("Búsqueda exitosa", f"Se encontró el alimento: {nombre}")

            # Reiniciar el ComboBox y limpiar el Entry
            self.combo_box.set("Seleccionar alimento")
            self.entry_buscar.delete(0, "end")
        else:
            messagebox.showwarning("Alimento no encontrado", "No se encontró el alimento en la base de datos.")
            print("Alimento no encontrado en la base de datos.")

    def buscar_alimento_en_db(self, nombre_alimento):
        conn = sqlite3.connect('alimentos.db')
        cursor = conn.cursor()
        
        query = "SELECT nombre, calorias_100g, calorias_porcion FROM alimentos WHERE nombre = ?"
        cursor.execute(query, (nombre_alimento,))
        
        resultado = cursor.fetchone()
        
        conn.close()
        
        return resultado
