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
        tabview = ctk.CTkTabview(self.panel_principal, width=800, height=550, fg_color='#404B4C', bg_color='#404B4C')
        tabview.place(relx=0.01, rely=0.005, relwidth=1, relheight=1)
        tab1 = tabview.add("Calorías vs Tiempo")
        tab2 = tabview.add("Peso vs Tiempo")
        tab3 = tabview.add("Agua vs Tiempo")
        self.crear_grafico_calorias(tab1)
        self.crear_grafico_peso(tab2)
        self.crear_grafico_agua(tab3)
        
    def crear_grafico_calorias(self, frame):
        fig = Figure(figsize=(8, 5), dpi=100, facecolor='#404B4C')
        ax1 = fig.add_subplot(111)
        fecha, cantidad = self.datos_calorias()
        ax1.set_facecolor(oscuro)
        ax1.grid(True, which='both', axis='y', linestyle='--', linewidth=0.6, color='gray')
        ax1.set_title('Calorías vs Tiempo', color='white', fontsize=12)
        ax1.set_ylabel('Calorías', color='white', fontsize=10)
        ax1.set_xlabel('Fecha', color='white', fontsize=10)

        if len(cantidad) > 0:
            bars = ax1.bar(fecha, cantidad, color=azul_mas_clarito, edgecolor='black', linewidth=1.5)
            for bar in bars:
                bar.set_linewidth(1.5)
                bar.set_edgecolor('white')
                bar.set_linestyle((0, (5, 1)))
            ax1.set_yticks(ax1.get_yticks())
        else:
            
            ax1.text(0.5, 0.5, 'No hay datos disponibles', horizontalalignment='center', 
                     verticalalignment='center', transform=ax1.transAxes, color='white', fontsize=12)
            ax1.set_yticks([])

        # Ajuste de ticks y etiquetas
        ax1.set_xticks(range(len(fecha)))  
        ax1.set_xticklabels(fecha, rotation=45, ha='right', fontsize=8, color='white')

        # Canvas
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        widget_canvas = canvas.get_tk_widget()
        widget_canvas.pack(fill='both', expand=True)

    def crear_grafico_peso(self, frame):
        fig = Figure(figsize=(8, 5), dpi=100, facecolor='#404B4C')
        ax2 = fig.add_subplot(111)
        fecha2, peso = self.datos_peso()
        ax2.set_facecolor(oscuro)
        ax2.grid(True, which='both', axis='y', linestyle='--', linewidth=0.6, color='gray')
        ax2.set_title('Peso vs Tiempo', color='white', fontsize=12)
        ax2.set_ylabel('Peso (kg)', color='white', fontsize=10)
        ax2.set_xlabel('Fecha', color='white', fontsize=10)

        if len(peso) > 0:
            ax2.plot(fecha2, peso, color=celeste_pero_oscuro, marker='o', markersize=6, markerfacecolor='white', linestyle='-', linewidth=2.5)
        else:
            
            ax2.text(0.5, 0.5, 'No hay datos disponibles', horizontalalignment='center', 
                     verticalalignment='center', transform=ax2.transAxes, color='white', fontsize=12)
            ax2.set_yticks([])

        # Ajuste de ticks y etiquetas
        ax2.set_xticks(range(len(fecha2)))  
        ax2.set_xticklabels(fecha2, rotation=45, ha='right', fontsize=8, color='white')

        # Canvas
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        widget_canvas = canvas.get_tk_widget()
        widget_canvas.pack(fill='both', expand=True)
        
    def crear_grafico_agua(self, frame):
        fig = Figure(figsize=(8, 5), dpi=100, facecolor='#404B4C')
        ax3 = fig.add_subplot(111)
        fecha3, agua = self.datos_agua()
        ax3.set_facecolor(oscuro)
        ax3.grid(True, which='both', axis='y', linestyle='--', linewidth=0.6, color='lightgray')
        ax3.set_title('Agua vs Tiempo', color='white', fontsize=12)
        ax3.set_ylabel('Agua', color='white', fontsize=10)
        ax3.set_xlabel('Fecha', color='white', fontsize=10)
        
        if len(agua) > 0:
            ax3.fill_between(fecha3, agua, color='#00BFFF', alpha=0.6)  
            ax3.plot(fecha3, agua, color='#00BFFF', linewidth=2)  
        else:
            
            ax3.text(0.5, 0.5, 'No hay datos disponibles', horizontalalignment='center', 
                     verticalalignment='center', transform=ax3.transAxes, color='white', fontsize=12)
            ax3.set_yticks([])

        # Ajuste de ticks y etiquetas
        ax3.set_xticks(range(len(fecha3)))  
        ax3.set_xticklabels(fecha3, rotation=45, ha='right', fontsize=8, color='white')

        # Canvas
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        widget_canvas = canvas.get_tk_widget()
        widget_canvas.pack(fill='both', expand=True)
        
        
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

    def datos_agua(self):
        conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
        cursor = conn.cursor()
        cursor.execute("SELECT fecha, cant FROM agua GROUP BY fecha")
        resultados = cursor.fetchall()
        conn.close()
        fecha3 = [fila[0] for fila in resultados]
        agua = [fila[1] for fila in resultados]
        return fecha3, agua
    