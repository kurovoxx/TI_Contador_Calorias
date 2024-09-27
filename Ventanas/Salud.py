from Ventanas.Ventana_interfaz import New_ventana
from util.colores import *
import customtkinter as ctk
import sqlite3
from CTkMessagebox import CTkMessagebox  # Importamos la librería para la messagebox

class Salud(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)
        # self.mostrar_messagebox()  # Llamamos a la función que muestra el mensaje al abrir la pestaña
        self.add_widget_salud()
  
    def add_widget_salud(self):
        # Botón "Actualizar Peso"
        self.btn_actualizar_peso = ctk.CTkButton(self.sub, text="Actualizar Peso", width=150, height=50, fg_color="gray")
        self.btn_actualizar_peso.place(x=50, y=50)

        # Botón "Medir pulsaciones"
        self.btn_medir_pulsaciones = ctk.CTkButton(self.sub, text="Medir pulsaciones", width=150, height=50, fg_color="gray")
        self.btn_medir_pulsaciones.place(x=50, y=150)

        # Botón "IMC" y "*IMC"
        self.label_imc = ctk.CTkLabel(self.sub, text="IMC: ", fg_color=None, text_color="black", font=("Arial", 15))
        self.label_imc.place(x=600, y=250)

        self.btn_imc_rojo = ctk.CTkButton(self.sub, text="Calcular IMC", width=100, height=50, fg_color="red", command=self.calcular_imc)
        self.btn_imc_rojo.place(x=600, y=50)

        # Botón "IBR" y "*IBR"
        self.btn_ibr = ctk.CTkButton(self.sub, text="IBR", width=100, height=50, fg_color="gray")
        self.btn_ibr.place(x=500, y=150)

        self.btn_ibr_rojo = ctk.CTkButton(self.sub, text="*IBR", width=100, height=50, fg_color="red")
        self.btn_ibr_rojo.place(x=600, y=150)

        # Crear los 8 botones redondeados debajo de la barra
        self.botones = []
        for i in range(8):
            boton = ctk.CTkButton(self.sub, text="", width=50, height=50, corner_radius=20, fg_color="gray", command=lambda b=i: self.toggle_color(self.botones[b]))
            boton.place(x=50 + i * 60, y=400)
            self.botones.append(boton)

        # Barra inferior
        self.barra_inferior = ctk.CTkProgressBar(self.sub, width=550, height=40, fg_color="gray", progress_color="green")
        self.barra_inferior.place(x=20, y=350)
        self.barra_inferior.set(0.7)

        # Etiquetas de Meta de Calorías y Vasos de Agua
        self.label_meta_calorias = ctk.CTkLabel(self.sub, text="Meta de Calorías x/Meta", fg_color=None, text_color="black", font=("Arial", 15))
        self.label_meta_calorias.place(x=600, y=350)

        self.label_vasos_agua = ctk.CTkLabel(self.sub, text="Vasos de Agua: x", fg_color=None, text_color="black", font=("Arial", 15))
        self.label_vasos_agua.place(x=600, y=420)

    def calcular_imc(self):
        try:
            conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
            cursor = conn.cursor()
            
            cursor.execute("SELECT estatura FROM datos")
            resultado_estatura = cursor.fetchone()
            if resultado_estatura is None:
                raise ValueError("No se encontró la estatura para el usuario")
            estatura = resultado_estatura[0]
            estatura = float(estatura / 100)

            cursor.execute("SELECT peso FROM peso ORDER BY fecha DESC LIMIT 1")
            resultado_peso = cursor.fetchone()
            if resultado_peso is None:
                raise ValueError("No se encontró el peso para el usuario")
            peso = resultado_peso[0]

            imc = peso / (estatura ** 2)
            self.label_imc.configure(text=f"IMC: {imc:.2f}")
            return imc

        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            self.label_imc.configure(text="Error al calcular IMC")
        except ValueError as e:
            print(f"Error de valor: {e}")
            self.label_imc.configure(text="Datos insuficientes para IMC")
        except Exception as e:
            print(f"Error inesperado: {e}")
            self.label_imc.configure(text="Error al calcular IMC")
        finally:
            if conn:
                conn.close()
    
    def calcular_TMB(self):
        try:
            conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
            cursor = conn.cursor()
            
            cursor.execute("SELECT estatura FROM datos")
            resultado_estatura = cursor.fetchone()
            if resultado_estatura is None:
                raise ValueError("No se encontró la estatura para el usuario")
            estatura = resultado_estatura[0]
            estatura = float(estatura / 100)

            cursor.execute("SELECT peso FROM peso ORDER BY fecha DESC LIMIT 1")
            resultado_peso = cursor.fetchone()
            if resultado_peso is None:
                raise ValueError("No se encontró el peso para el usuario")
            peso = resultado_peso[0]

            cursor.execute("SELECT edad FROM datos ORDER BY fecha DESC LIMIT 1")
            resultado_edad = cursor.fetchone()
            if resultado_edad is None:
                raise ValueError("No se encontró el peso para el usuario")
            edad = resultado_edad[0]

            cursor.execute("SELECT genero FROM datos")
            resultado_genero = cursor.fetchone()
            if resultado_genero is None:
                raise ValueError("No se encontró el sexo para el usuario")
            genero = resultado_genero[0]
            
            if genero == "hombre" or "masculino":
                tmb = 66 + (13.75 * peso) + (5 * estatura * 100) - (6.75 * edad)
            elif genero == "femenino" or "mujer":
                tmb = 655 + (9.56 * peso) + (1.85 * estatura * 100) - (4.67 * edad)
            else:
                raise ValueError("Sexo no válido")
            
            self.label_imc.configure(text=f"TMB: {tmb:.2f}")

            return tmb

        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            self.label_imc.configure(text="Error al calcular IMC")
        except ValueError as e:
            print(f"Error de valor: {e}")
            self.label_imc.configure(text="Datos insuficientes para IMC")
        except Exception as e:
            print(f"Error inesperado: {e}")
            self.label_imc.configure(text="Error al calcular IMC")
        finally:
            if conn:
                conn.close()

    def toggle_color(self, boton):
        # Cambiar entre verde y gris
        if boton.cget("fg_color") == "gray":  # Si el botón está gris
            boton.configure(fg_color="green")  # Cambia a verde
        else:
            boton.configure(fg_color="gray")  # Cambia a gris