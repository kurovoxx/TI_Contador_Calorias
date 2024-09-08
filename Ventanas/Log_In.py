import customtkinter as ctk
import os
from CTkMessagebox import CTkMessagebox
import sqlite3

class Log_in(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry('500x600')
        self.title('Log In')
        self.resizable(False, False)
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill='both', expand=True)
        self.limpiar_usuario()
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

        self.users_label = ctk.CTkLabel(self.frame_iniciar, text="Usuario:")
        self.users_label.pack(anchor="w", padx=3, pady=(2, 0))
        
        self.users_combobox = ctk.CTkComboBox(self.frame_iniciar, values=self.obtener_usuarios(), width=250, command=self.contra_aparecer)
        self.users_combobox.pack(padx=3, pady=(0, 2))

        self.btn_volver = ctk.CTkButton(self.frame_iniciar, text='Volver Atrás', command=self.add_widget_login)
        self.btn_volver.place(x=180, y=550)
    
    def win_registrar(self):
        self.limpiar_panel()

        self.frame_registrar = ctk.CTkFrame(self.main_frame, fg_color='yellow')
        self.frame_registrar.pack(fill='both', expand=True)

        self.nombre_label = ctk.CTkLabel(self.frame_registrar, text="Nombre:")
        self.nombre_label.pack(anchor="w", padx=3, pady=3)
        
        self.nombre_entry = ctk.CTkEntry(self.frame_registrar, placeholder_text="Introduce tu nombre", width=250)
        self.nombre_entry.pack(padx=3, pady=(0, 2))

        self.contra_label = ctk.CTkLabel(self.frame_registrar, text="Contraseña:")
        self.contra_label.pack(anchor="w", padx=3, pady=3)
        
        self.contra_entry = ctk.CTkEntry(self.frame_registrar, width=250, show="*")
        self.contra_entry.pack(padx=3, pady=(0, 2))

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

        self.crear_db(f"./users/{self.nombre_entry.get()}/alimentos.db")

        self.insertar_usuario(self.nombre_entry.get(), self.contra_entry.get())

        try:
            with open(f"./users/{self.nombre_entry.get()}/datos_usuario.txt", "a") as archivo_n:
                nombre = self.nombre_entry.get()
                archivo_n.write(f'{nombre}\n')

                edad = self.edad_entry.get()
                archivo_n.write(f'{edad}\n')

                sexo = self.gen_combobox.get()
                archivo_n.write(f'{sexo}\n')

                altura = self.altura_entry.get()
                archivo_n.write(f'{altura}\n')

                nivel_actividad = self.lvl_actividad_combobox.get()
                archivo_n.write(f'{nivel_actividad}\n')

            with open('usuario_actual.txt', 'w') as users:
                nombre = self.nombre_entry.get()
                users.write(f'{nombre}')
            
            CTkMessagebox(title="Exito", message="Se ha registrado correctamente",
                          icon='check',
                          option_1="Ok")
            
        except FileNotFoundError:
            CTkMessagebox(title="Advertencia", message="Error al registrarse.",
                          icon='warning', option_1="Ok")

    def limpiar_panel(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
    def crear_db(self, path):
        conn = sqlite3.connect(path)

        cursor = conn.cursor()

        cursor.execute('''
                CREATE TABLE IF NOT EXISTS alimento (
                    nombre TEXT NOT NULL,
                    calorias_100gr INTEGER,
                    calorias_porcion INTEGER
                )
                ''')

        cursor.execute('''
                CREATE TABLE IF NOT EXISTS consumo_diario (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    fecha TEXT NOT NULL,
                    hora TEXT NOT NULL
                )
                ''')
        
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS peso (
                    fecha TEXT PRIMARY KEY,
                    peso REAL
                )
                ''')
                
        conn.commit()
        conn.close()
        
    def insertar_usuario(self, nombre: str, contra: str):
        try:
            conn = sqlite3.connect('usuarios.db')
            cursor = conn.cursor()

            query = "INSERT INTO users (nombre, contra) VALUES (?, ?)"
            cursor.execute(query, (nombre, contra))

            conn.commit()

            CTkMessagebox(title="Exito", message="Se ha registrado correctamente",
                          icon='check',
                          option_1="Ok")

        except sqlite3.IntegrityError:
            CTkMessagebox(title="Advertencia", message="Nombre de usuario ocupado.",
                          icon='warning', option_1="Ok")
        
        finally:
            # Cerrar la conexión a la base de datos
            conn.close()

    def contra_aparecer(self, e):
        self.contra_label = ctk.CTkLabel(self.frame_iniciar, text="Contraseña:")
        self.contra_label.pack(anchor="w", padx=3, pady=3)
        
        self.contra_ingreso_entry = ctk.CTkEntry(self.frame_iniciar, width=250, show="*")
        self.contra_ingreso_entry.pack(padx=3, pady=(0, 2))

        self.guardar_button = ctk.CTkButton(self.frame_iniciar, text="Iniciar Sesión", command=self.verificar_contra, width=250)
        self.guardar_button.pack(pady=10)

    def obtener_usuarios(self):
        try:
            # Conectar a la base de datos 'users.db'
            conn = sqlite3.connect('usuarios.db')
            cursor = conn.cursor()

            # Ejecutar la consulta para obtener todos los nombres de usuario
            query = "SELECT nombre FROM users"
            cursor.execute(query)

            # Recuperar todos los resultados de la consulta
            usuarios = cursor.fetchall()

            # Devolver la lista de nombres de usuario
            # Extraemos solo el primer valor de cada fila (porque fetchall devuelve una lista de tuplas)
            lista_usuarios = [usuario[0] for usuario in usuarios]
            
            return lista_usuarios

        except sqlite3.Error as e:
            print(f"Error al obtener los usuarios: {e}")
            return []

        finally:
            # Cerrar la conexión a la base de datos
            conn.close()

    def verificar_contra(self):
            usuario = self.users_combobox.get()
            contra = self.contra_ingreso_entry.get()
            try:
                # Conectar a la base de datos 'users.db'
                conn = sqlite3.connect('usuarios.db')
                cursor = conn.cursor()

                query = "SELECT contra FROM users WHERE nombre = ?"
                cursor.execute(query, (usuario,))

                resultado = cursor.fetchone()

                if resultado:
                    # La contraseña en la base de datos es el primer valor de la tupla 'resultado'
                    contraseña_correcta = resultado[0]

                    # Verificar si la contraseña ingresada coincide con la almacenada
                    if contra == contraseña_correcta:
                        CTkMessagebox(title="Exito", message=f"Ha iniciado sesión como {usuario}",
                          icon='check',
                          option_1="Ok")
                        return True
                    else:
                        CTkMessagebox(title="Advertencia", message="Contraseña incorrecta.",
                          icon='warning', option_1="Ok")
                        return False
                else:
                    print("Error", "Usuario no encontrado.")
                    return False

            except sqlite3.Error as e:
                print(f"Error al verificar la contraseña: {e}")
                return False

            finally:
                conn.close()
            pass
    
    def limpiar_usuario(self):
        with open('usuario_actual.txt', 'w') as users:
                users.write('')