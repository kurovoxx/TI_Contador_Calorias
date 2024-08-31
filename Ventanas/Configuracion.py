import customtkinter as ctk
from Ventanas.Ventana_interfaz import New_ventana


class Configuracion(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)
        self.add_widget_config()
        self.contruirWidget()

    def add_widget_config(self):
        self.perfil_frame = ctk.CTkFrame(self.sub, corner_radius=10) #se usa .sub envez de solamente el self
        self.perfil_frame.pack(padx=20, pady=10, fill="x", expand=True)

        # widgets, uno debajo del otro
        self.nombre_label = ctk.CTkLabel(self.perfil_frame, text="Nombre:")
        self.nombre_label.pack(anchor="w", padx=3, pady=3)
        self.nombre_entry = ctk.CTkEntry(self.perfil_frame, placeholder_text="Introduce tu nombre")
        self.nombre_entry.pack(fill="x", padx=3, pady=(0, 2))

        self.edad_label = ctk.CTkLabel(self.perfil_frame, text="Edad:")
        self.edad_label.pack(anchor="w", padx=3, pady=(2, 0))
        self.edad_entry = ctk.CTkEntry(self.perfil_frame, placeholder_text="Introduce tu edad")
        self.edad_entry.pack(fill="x", padx=3, pady=(0, 2))

        self.gen_label = ctk.CTkLabel(self.perfil_frame, text="Sexo:")
        self.gen_label.pack(anchor="w", padx=3, pady=(2, 0))
        self.gen_combobox = ctk.CTkComboBox(self.perfil_frame, values=["Masculino", "Femenino", "Otro"])
        self.gen_combobox.pack(fill="x", padx=3, pady=(0, 2))

        self.peso_label = ctk.CTkLabel(self.perfil_frame, text="Peso (kg):")
        self.peso_label.pack(anchor="w", padx=3, pady=(2, 0))
        self.peso_entry = ctk.CTkEntry(self.perfil_frame, placeholder_text="Introduce tu peso")
        self.peso_entry.pack(fill="x", padx=3, pady=(0, 2))

        self.altura_label = ctk.CTkLabel(self.perfil_frame, text="Altura (cm):")
        self.altura_label.pack(anchor="w", padx=3, pady=(2, 0))
        self.altura_entry = ctk.CTkEntry(self.perfil_frame, placeholder_text="Introduce tu altura")
        self.altura_entry.pack(fill="x", padx=3, pady=(0, 2))

        self.obj_calorias_label = ctk.CTkLabel(self.perfil_frame, text="Objetivo de Calorías:")
        self.obj_calorias_label.pack(anchor="w", padx=3, pady=(2, 0))
        self.obj_calorias_combobox = ctk.CTkComboBox(self.perfil_frame, values=["Pérdida de peso", "Mantenimiento", "Aumento de peso"])
        self.obj_calorias_combobox.pack(fill="x", padx=3, pady=(0, 2))

        self.lvl_actividad_label = ctk.CTkLabel(self.perfil_frame, text="Nivel de Actividad:")
        self.lvl_actividad_label.pack(anchor="w", padx=3, pady=(2, 0))
        self.lvl_actividad_combobox = ctk.CTkComboBox(self.perfil_frame, values=["Sedentario", "Ligero", "Moderado", "Intenso"])
        self.lvl_actividad_combobox.pack(fill="x", padx=3, pady=(0, 2))

        self.guardar_button = ctk.CTkButton(self.sub, text="Guardar", command=self.guardar)
        self.guardar_button.pack(pady=5)

    def contruirWidget(self):
        self.info_frame = ctk.CTkFrame(self.sub, corner_radius=10)
        self.info_frame.pack(padx=5, pady=5, fill="x", expand=True)
        
        self.labelVersion = ctk.CTkLabel(self.info_frame, text="Version : 1.0")
        self.labelVersion.pack(pady=3)

        self.labelAutor = ctk.CTkLabel(self.info_frame, text="Autor : Los insanos 2.0")
        self.labelAutor.pack(pady=3)

    def guardar(self):
        nombre = self.nombre_entry.get()
        edad = self.edad_entry.get()
        sexo = self.gen_combobox.get()
        peso = self.peso_entry.get()
        altura = self.altura_entry.get()
        objetivo_calorias = self.obj_calorias_combobox.get()
        nivel_actividad = self.lvl_actividad_combobox.get()

        print(f"Nombre: {nombre}, Edad: {edad}, Sexo: {sexo}, Peso: {peso}, Altura: {altura}, "
              f"Objetivo de Calorías: {objetivo_calorias}, Nivel de Actividad: {nivel_actividad}")
