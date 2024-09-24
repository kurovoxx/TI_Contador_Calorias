import customtkinter as ctk
from Ventanas.Ventana_interfaz import New_ventana
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import sqlite3
from util.colores import *

class Grafico(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)
        self.panel_principal = panel_principal
        self.add_widget_graficos()

    def add_widget_graficos(self):
        fig = Figure(figsize=(10, 5), dpi=100, facecolor='#404B4C')
        fig.subplots_adjust(wspace=0.4)
        ax1 = fig.add_subplot(121)  
        ax2 = fig.add_subplot(122)  
        
        fecha, cantidad = self.datos_calorias()
        ax1.set_facecolor('#404B4C')
        ax1.bar(fecha, cantidad, color='blue', edgecolor='black')
        ax1.grid(True, which='both', axis='y', linestyle='--', linewidth=0.7, color='black')
        ax1.set_title('Gráfico calorías vs tiempo', color='white')
        ax1.set_ylabel('Calorías', color='white')
        ax1.set_xlabel('Fecha', color='white')
        ax1.tick_params(axis='x', rotation=45, labelsize=8) 

        fecha2, peso = self.datos_peso()
        ax2.set_facecolor('#404B4C')
        ax2.plot(fecha2, peso, color='green', marker='o') 
        ax2.grid(True, which='both', axis='y', linestyle='--', linewidth=0.7, color='black')
        ax2.set_title('Gráfico peso vs tiempo', color='white')
        ax2.set_ylabel('Peso (kg)', color='white')
        ax2.set_xlabel('Fecha', color='white')
        ax2.tick_params(axis='x', rotation=45, labelsize=8) 

        canvas = FigureCanvasTkAgg(fig, master=self.panel_principal)
        canvas.draw()
        widget_canvas = canvas.get_tk_widget()
        widget_canvas.place(x=50, y=50, width=800, height=550)

    def datos_calorias(self):
        conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(total_cal), fecha FROM consumo_diario GROUP BY fecha")
        resultados = cursor.fetchall()
        conn.close()
        cantidad = [fila[0] for fila in resultados]
        fecha = [fila[1] for fila in resultados]
        return fecha, cantidad

    def datos_peso(self):
        conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
        cursor = conn.cursor()
        cursor.execute("SELECT fecha, peso FROM peso GROUP BY fecha")
        resultados = cursor.fetchall()
        conn.close()
        fecha2 = [fila[0] for fila in resultados]
        peso = [fila[1] for fila in resultados]
        return fecha2, peso
