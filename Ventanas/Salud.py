from Ventanas.Ventana_interfaz import New_ventana
from Ventanas.update_peso import Peso
from util.colores import *
import customtkinter as ctk
import sqlite3
from CTkMessagebox import CTkMessagebox

class Salud(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)
        self.mostrar_messagebox()
        self.add_widget_salud()
        self.update_health_metrics()

    def mostrar_messagebox(self):
        mensaje = ("Bienvenido a la sección Salud. Aquí podrás actualizar tu peso, medir pulsaciones, "
                   "calcular tu IMC Y TMB, además de realizar un seguimiento de tu progreso diario. "
                   "Usa los botones y la barra de progreso para monitorear tus metas.")
        CTkMessagebox(title="Sección Salud", message=mensaje, icon="info", option_1="OK")

    def add_widget_salud(self):
        # Botón "Actualizar Peso"
        self.btn_actualizar_peso = ctk.CTkButton(self.sub, text="Actualizar Peso", width=150, height=50, fg_color="#28242c", command=self.actualizar_peso)
        self.btn_actualizar_peso.place(x=50, y=50)

        # Botón "Medir pulsaciones"
        self.btn_medir_pulsaciones = ctk.CTkButton(self.sub, text="Medir pulsaciones", width=150, height=50, fg_color="#28242c")
        self.btn_medir_pulsaciones.place(x=50, y=150)

        self.label_imc = ctk.CTkLabel(self.sub, text="IMC:", fg_color="#28242c", text_color="white", font=("Arial", 15), width=100, height=50)
        self.label_imc.configure(corner_radius=5)
        self.label_imc.place(x=500, y=50)

        self.result_imc = ctk.CTkLabel(self.sub, text="", fg_color="#28242c", text_color="white", font=("Arial", 15), width=100, height=50)
        self.result_imc.place(x=610, y=50)

        self.label_tmb = ctk.CTkLabel(self.sub, text="TMB:", fg_color="#28242c", text_color="white", font=("Arial", 15), width=100, height=50)
        self.label_tmb.configure(corner_radius=5)
        self.label_tmb.place(x=500, y=150)
        
        self.result_tmb = ctk.CTkLabel(self.sub, text="", fg_color="#28242c", text_color="white", font=("Arial", 15), width=100, height=50)
        self.result_tmb.place(x=610, y=150)

        # Crear los 8 botones redondeados debajo de la barra
        self.botones = []
        self.estado_botones = [False] * 8

        for i in range(8):
            boton = ctk.CTkButton(self.sub, text="", width=50, height=50, corner_radius=20, fg_color="#28242c", 
                                  command=lambda b=i: self.toggle_color(b))
            boton.place(x=50 + i * 60, y=400)
            self.botones.append(boton)

        # Barra inferior
        self.barra_inferior = ctk.CTkProgressBar(self.sub, width=550, height=40, fg_color="#417156", progress_color="#ade28a")
        self.barra_inferior.place(x=20, y=350)
        self.barra_inferior.set(0.7)

        # Etiquetas de Meta de Calorías y Vasos de Agua
        self.label_meta_calorias = ctk.CTkLabel(self.sub, text="Meta de Calorías x/Meta", fg_color=None, text_color="black", font=("Arial", 15))
        self.label_meta_calorias.place(x=600, y=350)

        self.label_vasos_agua = ctk.CTkLabel(self.sub, text="Vasos de Agua: x", fg_color=None, text_color="black", font=("Arial", 15))
        self.label_vasos_agua.place(x=600, y=420)

    def toggle_color(self, indice):
        if self.estado_botones[indice]:
            self.botones[indice].configure(fg_color="#28242c")
            self.estado_botones[indice] = False
        else:
            self.botones[indice].configure(fg_color="green")
            self.estado_botones[indice] = True
    
    def actualizar_peso(self):
        Peso(self.sub, self.usuario, callback=self.update_health_metrics)

    def get_latest_weight(self):
        try:
            conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
            cursor = conn.cursor()
            
            cursor.execute("SELECT peso FROM peso ORDER BY fecha DESC LIMIT 1")
            result = cursor.fetchone()
            
            if result is None:
                raise ValueError("No se encontró ningún registro de peso")
            
            return result[0]
        except (sqlite3.Error, ValueError) as e:
            print(f"Error al obtener el peso más reciente: {e}")
            return None
        finally:
            if conn:
                conn.close()

    def calcular_imc(self):
        try:
            conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
            cursor = conn.cursor()
            
            cursor.execute("SELECT estatura FROM datos")
            resultado_estatura = cursor.fetchone()
            if resultado_estatura is None:
                raise ValueError("No se encontró la estatura para el usuario")
            estatura = resultado_estatura[0] / 100  # Convertir a metros

            cursor.execute("SELECT peso FROM peso WHERE num = (SELECT MAX(num) FROM peso)")
            resultado_peso = cursor.fetchone()
            if resultado_peso is None:
                raise ValueError("No se encontró ningún registro de peso")
            peso = resultado_peso[0]

            imc = peso / (estatura ** 2)
            return imc

        except (sqlite3.Error, ValueError) as e:
            print(f"Error al calcular IMC: {e}")
            return None
        finally:
            if conn:
                conn.close()

    def calcular_TMB(self):
        try:
            conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
            cursor = conn.cursor()
            
            cursor.execute("SELECT estatura, edad, genero FROM datos")
            result = cursor.fetchone()
            if result is None:
                raise ValueError("No se encontraron datos del usuario")
            estatura, edad, genero = result
            estatura = estatura / 100  # Convertir a metros

            cursor.execute("SELECT peso FROM peso WHERE num = (SELECT MAX(num) FROM peso)")
            resultado_peso = cursor.fetchone()
            if resultado_peso is None:
                raise ValueError("No se encontró ningún registro de peso")
            peso = resultado_peso[0]

            if genero.lower() in ["hombre", "masculino"]:
                tmb = 66 + (13.75 * peso) + (5 * estatura * 100) - (6.75 * edad)
            elif genero.lower() in ["mujer", "femenino"]:
                tmb = 655 + (9.56 * peso) + (1.85 * estatura * 100) - (4.67 * edad)
            else:
                raise ValueError("Género no válido")
            
            return tmb

        except (sqlite3.Error, ValueError) as e:
            print(f"Error al calcular TMB: {e}")
            return None
        finally:
            if conn:
                conn.close()

    def update_health_metrics(self):
        imc = self.calcular_imc()
        tmb = self.calcular_TMB()

        if imc is not None:
            self.result_imc.configure(text=f"{imc:.2f}")
        else:
            self.result_imc.configure(text="Error")

        if tmb is not None:
            self.result_tmb.configure(text=f"{tmb:.2f}")
        else:
            self.result_tmb.configure(text="Error")
        
        self.sub.update()
