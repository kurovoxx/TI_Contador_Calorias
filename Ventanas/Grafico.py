from Ventanas.Ventana_interfaz import New_ventana
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class Grafico(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color)
        self.panel_principal = panel_principal # Para asignar el grafico, esto de momento lo hice así 
        self.add_widget_grafico()

    def add_widget_grafico(self):
        fig = Figure(figsize=(5, 4), dpi=100,facecolor='#404B4C') # color del fondo de los ejes creo (siera)
        ax = fig.add_subplot(111)
        # Color del fondo (dentro)
        ax.set_facecolor('#404B4C') 
        # Acá deben ir los cosos estos BD agustin del futuro
        categorias = ['hola', 'adios', 'que', 'so']
        valores = [10, 20, 15, 25]
        ax.bar(categorias, valores, color='blue', edgecolor='black')  # Edgecolor es el borde
        ax.set_title('Gráfico de ejemplo', color='white')  
        ax.set_ylabel('Nombre Y', color='white')        
        ax.set_xlabel('Nombre X', color='white')          
        canvas = FigureCanvasTkAgg(fig, master=self.panel_principal)
        canvas.draw()
        widget_canvas = canvas.get_tk_widget()
        widget_canvas.place(x=50, y=100, width=400, height=400)  
