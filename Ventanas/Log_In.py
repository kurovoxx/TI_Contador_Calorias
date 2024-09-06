import customtkinter as ctk
import os

class Log_in(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry('500x600')
        self.title('Log In')
        self.resizable(False, False)
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill='both', expand=True)
        self.add_widget_login()

    def add_widget_login(self):
        self.limpiar_panel()

        self.frame = ctk.CTkFrame(self.main_frame, fg_color='red')
        self.frame.pack(fill='both', expand=True)

        self.btn_iniciar = ctk.CTkButton(self.frame, text='Iniciar Sesión', width=170, height=50, command=self.win_iniciar)
        self.btn_iniciar.place(x= 170, y=100)

        self.btn_registrarse = ctk.CTkButton(self.frame, text='Registrarse', width=170, height=50, command=self.win_registrar)
        self.btn_registrarse.place(x=170, y=180)
    
    def win_iniciar(self):
        self.limpiar_panel()

        self.frame_iniciar = ctk.CTkFrame(self.main_frame, fg_color='blue')
        self.frame_iniciar.pack(fill='both', expand=True)

        self.btn_volver = ctk.CTkButton(self.frame_iniciar, text='Volver Atrás', command=self.add_widget_login)
        self.btn_volver.place(x=180, y=300)
    
    def win_registrar(self):
        self.limpiar_panel()

        self.frame_registrar = ctk.CTkFrame(self.main_frame, fg_color='yellow')
        self.frame_registrar.pack(fill='both', expand=True)

        self.nombre_label = ctk.CTkLabel(self.frame_registrar, text="Nombre:")
        self.nombre_label.pack(anchor="w", padx=3, pady=3)
        
        self.nombre_entry = ctk.CTkEntry(self.frame_registrar, placeholder_text="Introduce tu nombre", width=250)
        self.nombre_entry.pack(padx=3, pady=(0, 2))

        self.edad_label = ctk.CTkLabel(self.frame_registrar, text="Edad:")
        self.edad_label.pack(anchor="w", padx=3, pady=(2, 0))
        
        self.edad_entry = ctk.CTkEntry(self.frame_registrar, placeholder_text="Introduce tu edad", width=250)
        self.edad_entry.pack(padx=3, pady=(0, 2))

        self.gen_label = ctk.CTkLabel(self.frame_registrar, text="Sexo:")
        self.gen_label.pack(anchor="w", padx=3, pady=(2, 0))
        
        self.gen_combobox = ctk.CTkComboBox(self.frame_registrar, values=["Masculino", "Femenino", "Otro"], width=250)
        self.gen_combobox.pack(padx=3, pady=(0, 2))

        self.peso_label = ctk.CTkLabel(self.frame_registrar, text="Peso (kg):")
        self.peso_label.pack(anchor="w", padx=3, pady=(2, 0))
        
        self.peso_entry = ctk.CTkEntry(self.frame_registrar, placeholder_text="Introduce tu peso", width=250)
        self.peso_entry.pack(padx=3, pady=(0, 2))

        self.altura_label = ctk.CTkLabel(self.frame_registrar, text="Altura (cm):")
        self.altura_label.pack(anchor="w", padx=3, pady=(2, 0))
        
        self.altura_entry = ctk.CTkEntry(self.frame_registrar, placeholder_text="Introduce tu altura", width=250)
        self.altura_entry.pack(padx=3, pady=(0, 2))

        self.lvl_actividad_label = ctk.CTkLabel(self.frame_registrar, text="Nivel de Actividad:")
        self.lvl_actividad_label.pack(anchor="w", padx=3, pady=(2, 0))
        
        self.lvl_actividad_combobox = ctk.CTkComboBox(self.frame_registrar, values=["Sedentario", "Ligero", "Moderado", "Intenso"], width=250)
        self.lvl_actividad_combobox.pack(padx=3, pady=(0, 2))

        self.guardar_button = ctk.CTkButton(self.frame_registrar, text="Guardar", command=self.guardar, width=250)
        self.guardar_button.pack(pady=10)

        self.btn_volver = ctk.CTkButton(self.frame_registrar, text='Volver Atrás', command=self.add_widget_login)
        self.btn_volver.pack(pady=10)
        
    def guardar(self):

        directorio = f'./users/{self.nombre_entry.get()}'

        os.makedirs(directorio, exist_ok=True)

        try:
            with open(f"./users/{self.nombre_entry.get()}/datos_usuario.txt", "a") as archivo_n:
                nombre = self.nombre_entry.get()
                archivo_n.write(f'{nombre}\n')

                edad = self.edad_entry.get()
                archivo_n.write(f'{edad}\n')

                sexo = self.gen_combobox.get()
                archivo_n.write(f'{sexo}\n')

                peso = self.peso_entry.get()
                archivo_n.write(f'{peso}\n')

                altura = self.altura_entry.get()
                archivo_n.write(f'{altura}\n')

                nivel_actividad = self.lvl_actividad_combobox.get()
                archivo_n.write(f'{nivel_actividad}\n')

            messagebox.showinfo("Confirmación", "Los datos se guardaron correctamente.")
            
        except FileNotFoundError:
            messagebox.showerror("Error", "Hubo un problema al guardar los datos.")

    def limpiar_panel(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()