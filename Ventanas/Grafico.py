from Ventanas.Ventana_interfaz import New_ventana
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import sqlite3

class Grafico(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)
        self.panel_principal = panel_principal
        self.add_widget_grafico()

    def add_widget_grafico(self):
        fig = Figure(figsize=(5, 4), dpi=100, facecolor='#404B4C') # Color del fondo de los ejes (fuera de la "zona" de barras)
        ax = fig.add_subplot(111)
        
        # Color del fondo (dentro de la "zona" de barras)
        ax.set_facecolor('#404B4C') 
        
        # Datos por la consulta
        fecha, cantidad = self.probando()

        ax.bar(fecha, cantidad, color='blue', edgecolor='black')  # Color barras y edgecolor es el borde
        ax.grid(True, which='both', axis='y', linestyle='--', linewidth=0.7, color='black') # Esto es para las lineas que salen de valores
        ax.set_title('Gráfico calorías vs tiempo', color='white')  
        ax.set_ylabel('Calorias', color='white')        
        ax.set_xlabel('Fecha', color='white')          
        canvas = FigureCanvasTkAgg(fig, master=self.panel_principal)
        canvas.draw()
        widget_canvas = canvas.get_tk_widget()
        widget_canvas.place(x=200, y=100, width=600, height=400)  

    def probando(self):
        conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(total_cal), fecha FROM consumo_diario GROUP BY fecha")
        resultados = cursor.fetchall()
        conn.close()
        cantidad = [fila[0] for fila in resultados]
        fecha = [fila[1] for fila in resultados]
        return fecha, cantidad
    