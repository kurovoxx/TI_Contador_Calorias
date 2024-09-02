import tkinter as tk 
from tkinter import font
import datetime  as dt
from colores import *
import util.util_ventana as util_ventana
import util.util_imagenes as util_img

from Ventanas.Registro_Alimento import Registro_Alimento
from Ventanas.Agregar_Alimento import Agregar_Alimento
from Ventanas.Grafico import Grafico
from Ventanas.Historial import Historial
from Ventanas.Configuracion import Configuracion


class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.logo = util_img.leer_imagen("./img/logo1.png", (800, 800))
        self.perfil = util_img.leer_imagen("./img/sin_imagen.png", (100, 100))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_barra_lateral()
        self.controles_cuerpo()
        
    def config_window(self):
        self.title('Contador de Calorias Pro 60Hz')
        self.iconbitmap("./img/logo2.ico")
        w, h = 1024, 600
        util_ventana.centrar_ventana(self, w, h)

    def paneles(self):
        # Crear paneles: Barra superior, Menu lateral y cuerpo principal
        self.barra_superior = tk.Frame(
            self, bg=COLOR_BARRA_SUPERIOR, height=200)
        self.barra_superior.pack(side=tk.TOP, fill='both')
        
        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)
        
        self.cuerpo_principal = tk.Frame(
            self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)
        
    def controles_barra_superior(self):
        # Configuración de la barra superior
        font_awesome = font.Font(family='FontAwesome', size=12)
        
        #etiqueta de titulo
        self.labelTitutlo = tk.Label(self.barra_superior, text= "Contador calorias")
        self.labelTitutlo.config(fg="#fff",font=(
            "Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
        self.labelTitutlo.pack(side=tk.LEFT)
        
        # boton del menu lateral
        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome,
                                           command=self.toglle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)
        
        # Fecha bien pro
        tiempo = dt.datetime.now()
        
        #Etiqueta de información
        self.labelTitutlo = tk.Label(
            self.barra_superior, text="{}/{}/{}".format(tiempo.day,tiempo.month,tiempo.year))
        self.labelTitutlo.config(fg="#fff", font=(
            "Roboto", 15), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.labelTitutlo.pack(side=tk.RIGHT)
        
    def controles_barra_lateral(self):
        # Configuración del menu lateral
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)
        
        # Etiqueta de perfil
        self.labelPerfil = tk.Label(
            self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady=10)
        
        # Botoenes del menú lateral
        
        self.btn_registro = tk.Button(self.menu_lateral)
        self.btn_agregar = tk.Button(self.menu_lateral)
        self.btn_grafico = tk.Button(self.menu_lateral)
        self.btn_historial = tk.Button(self.menu_lateral)
        self.btn_en_contruccion = tk.Button(self.menu_lateral)
        
        buttons_info = [
            ("Registrar Alimento", "\uf109", self.btn_registro, self.abrir_registro_alimento),
            ("Agregar Alimento", "\uf007", self.btn_agregar, self.abrir_agregar_alimento),
            ("Gráfico", "\uf03e", self.btn_grafico, self.abrir_grafico),
            ("Historial", "\uf129", self.btn_historial, self.abrir_historial),
            ("Settings", "\uf013", self.btn_en_contruccion, self.abrir_configuracion)
        ]
        
        for text, icon, button, comando in buttons_info:
            self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu, comando)

    def controles_cuerpo(self):
        # Imagen en el cuerpo principal
        label = tk.Label(self.cuerpo_principal, image=self.logo,
                         bg=COLOR_CUERPO_PRINCIPAL)
        label.place(x=0, y=0, relwidth=1, relheight=1)
            
    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu, comando):
        button.config(text=f" {icon}    {text}", anchor="w", font=font_awesome,
                      bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu,
                      command=comando)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)
        
    def bind_hover_events(self, button):
        # Asociar eventos Enter y Leave con la función dinámica
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))
        
    def on_enter(self, event, button):
        # Cambiar estilo al pasar el raton por encima
        button.config(bg= COLOR_MENU_CURSOR_ENCIMA, fg='white')
        
    def on_leave(self, event, button):
        # Restaurar el estilo al salir el raton
        button.config(bg=COLOR_MENU_LATERAL, fg='white')
        
    def toglle_panel(self):
        # Alternar visibilidad del menú lateral
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')

    def abrir_registro_alimento(self):
        self.limpiar_panel(self.cuerpo_principal)
        Registro_Alimento(self.cuerpo_principal, '#404B4C')
        
    def abrir_agregar_alimento(self):
        self.limpiar_panel(self.cuerpo_principal)
        Agregar_Alimento(self.cuerpo_principal, '#404B4C')

    def abrir_grafico(self):
        self.limpiar_panel(self.cuerpo_principal)
        Grafico(self.cuerpo_principal, 'orange')

    def abrir_historial(self):
        self.limpiar_panel(self.cuerpo_principal)
        Historial(self.cuerpo_principal, 'black')

    def abrir_configuracion(self):
        self.limpiar_panel(self.cuerpo_principal)
        Configuracion(self.cuerpo_principal, '#404B4C')    
    
    def abrir_panel_en_construccion(self):
        print('Nada por aquí...')

    def limpiar_panel(self, panel):
        for widget in panel.winfo_children():
            widget.destroy()

    def abrir_panel_info(self):
        pass
 
