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
        # Crear figura
        fig = Figure(figsize=(10, 5), dpi=100, facecolor='#404B4C')
        fig.subplots_adjust(wspace=0.4)
        ax1 = fig.add_subplot(121)
        fecha, cantidad = self.datos_calorias()
        
        # Datos (BD)
        ax1.set_facecolor(oscuro)
        ax2 = fig.add_subplot(122)
        fecha2, peso = self.datos_peso()
        ax2.set_facecolor(oscuro)
        
        # Configuración de los ejes
        ax1.grid(True, which='both', axis='y', linestyle='--', linewidth=0.6, color='gray')
        ax1.set_title('Calorías vs Tiempo', color='white', fontsize=12)
        ax1.set_ylabel('Calorías', color='white', fontsize=10)
        ax1.set_xlabel('Fecha', color='white', fontsize=10)
        ax2.grid(True, which='both', axis='y', linestyle='--', linewidth=0.6, color='gray')
        ax2.set_title('Peso vs Tiempo', color='white', fontsize=12)
        ax2.set_ylabel('Peso (kg)', color='white', fontsize=10)
        ax2.set_xlabel('Fecha', color='white', fontsize=10)
        
        
        # Ocultar numeros en caso de no haber datos (Eje Y)
        if len(cantidad) > 0:
            bars = ax1.bar(fecha, cantidad, color=azul_mas_clarito, edgecolor='black', linewidth=1.5)
            for bar in bars:
                bar.set_linewidth(1.5)
                bar.set_edgecolor('white')
                bar.set_linestyle((0, (5, 1)))
            ax1.set_yticks(ax1.get_yticks())
        else:
            ax1.set_yticks([])  
        if len(peso) > 0:
            ax2.plot(fecha2, peso, color=celeste_pero_oscuro, marker='o', markersize=6, markerfacecolor='white', linestyle='-', linewidth=2.5)
        else:
            ax2.set_yticks([])
        
        # Desplazamiento de etiquetas
        x_locs_barras = [bar.get_x() + bar.get_width() / 2 for bar in bars] if len(cantidad) > 0 else []
        desplazamiento_barras = 0.2
        x_locs_adjusted_barras = [x + desplazamiento_barras for x in x_locs_barras]
        ax1.set_xticks(x_locs_adjusted_barras)
        ax1.set_xticklabels(fecha, rotation=45, ha='right', fontsize=8, color='white')
        x_locs_lineas = range(len(fecha2))
        desplazamiento_lineas = 0.1
        x_locs_adjusted_lineas = [x + desplazamiento_lineas for x in x_locs_lineas]
        ax2.set_xticks(x_locs_adjusted_lineas)
        ax2.set_xticklabels(fecha2, rotation=45, ha='right', fontsize=8, color='white')
        
        # Canvas
        canvas = FigureCanvasTkAgg(fig, master=self.panel_principal)
        canvas.draw()
        widget_canvas = canvas.get_tk_widget()
        widget_canvas.place(x=50, y=10, width=800, height=600)

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
