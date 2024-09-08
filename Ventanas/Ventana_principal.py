import tkinter as tk 
from tkinter import *
from tkinter import font, filedialog
import customtkinter as ctk
from datetime import datetime
from colores import *
import util.util_ventana as util_ventana
import util.util_imagenes as util_img
from PIL import Image, ImageDraw, ImageTk
import json

from Ventanas.Registro_Alimento import Registro_Alimento
from Ventanas.Agregar_Alimento import Agregar_Alimento
from Ventanas.Grafico import Grafico
from Ventanas.Historial import Historial
from Ventanas.Configuracion import Configuracion
from Ventanas.Log_In import Log_in



class Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.logo = util_img.leer_imagen("./img/logo1.png", (800, 800))
        self.config_window()
        self.esperando_login()
        self.log_in()
        
    def config_window(self):
        self.title('Contador de Calorias Pro 60Hz')
        self.iconbitmap("./img/logo2.ico")
        w, h = 1024, 600
        util_ventana.centrar_ventana(self, w, h)

    def cargar_main(self):
        self.paneles()
        self.perfil = self.cargar_imagen_guardada()
        self.controles_barra_superior()
        self.controles_barra_lateral()
        self.controles_cuerpo()

    def paneles(self):
        self.frame_tapar.destroy()
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
        
        
        #Etiqueta de información
        self.labelTitutlo = tk.Label(
            self.barra_superior, text='Hoy es: ' + datetime.now().strftime('%d-%m-%Y'))
        self.labelTitutlo.config(fg="#fff", font=(
            "Roboto", 15), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.labelTitutlo.pack(side=tk.RIGHT)

    def seleccionar_archivo(self):
        archivo = filedialog.askopenfilename(filetypes=[("Imagen", "*.png .jpg .jpeg")])
        if archivo:
            print(f"Archivo seleccionado: {archivo}")
            # Cargar la imagen seleccionada usando PIL directamente
            imagen_perfil = Image.open(archivo).resize((100, 100))  # Asegúrate de que esto devuelve un objeto de tipo Image
            imagen_perfil_circular = self.hacer_imagen_circular(imagen_perfil)
            self.perfil = ImageTk.PhotoImage(imagen_perfil_circular)  # Asignar la imagen a self.perfil
            self.labelPerfil.config(image=self.perfil)
            with open("imagen_seleccionada.json", "w") as f:
                json.dump({"ruta_imagen": archivo}, f)
    
    def cargar_imagen_guardada(self):
        try:
            with open("imagen_seleccionada.json", "r") as f:
                data = json.load(f)
                ruta_imagen = data.get("ruta_imagen")
                if ruta_imagen:
                    # Cargar y mostrar la imagen
                    img = Image.open(ruta_imagen).convert('RGBA')
                    img = self.hacer_imagen_circular(img)
                    img_tk = ImageTk.PhotoImage(img, format='PNG') # <--- Agregué format='PNG'
                    etiqueta_imagen = tk.Label(self.menu_lateral, image=img_tk)
                    etiqueta_imagen.image = img_tk
                    etiqueta_imagen.pack()

                    self.perfil = img_tk  # Asignar la imagen a self.perfil
        except FileNotFoundError:
            print("no hay archivo seleccionado")
            img_noperfil = util_img.leer_imagen("./img/sin_imagen.png", (100, 100))
            etiqueta_imagen = tk.Label(self.menu_lateral, image=img_noperfil)
            etiqueta_imagen.image = img_noperfil
            etiqueta_imagen.pack()
        
            self.perfil = img_noperfil  # Asignar la imagen a self.perfil

    def hacer_imagen_circular(self, imagen):
    # Crear una máscara circular
        mascarilla = Image.new("L", (120, 120), 0)  # Ajustar tamaño aquí
        dibujar = ImageDraw.Draw(mascarilla)
        dibujar.ellipse((0, 0, 120, 120), fill=255)  # Ajustar tamaño aquí

        # Aplicar la máscara a la imagen
        imagen_circular = Image.new("RGBA", (120, 120))  # Ajustar tamaño aquí
        imagen_circular.paste(imagen.resize((120, 120)), (0, 0), mascarilla)  # Ajustar tamaño aquí

        return imagen_circular

    def controles_barra_lateral(self):
        # Configuración del menu lateral
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)
        
        self.labelPerfil = tk.Label(self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady=10)
        self.btn_mas = tk.Button(self.menu_lateral, 
                         text="+", 
                         font=("Arial", 15), 
                         bg="#34A85A", 
                         fg="white", 
                         relief="flat", 
                         borderwidth=0,
                         command=self.seleccionar_archivo)
        self.btn_mas.place(x=130, y=90, width=20, height=20)
  
        # Botones del menú lateral
        
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
        Historial(self.cuerpo_principal, '#404B4C')

    def abrir_configuracion(self):
        self.limpiar_panel(self.cuerpo_principal)
        Configuracion(self.cuerpo_principal, '#404B4C')   

    def log_in(self):
        Log_in(self)

    def abrir_panel_en_construccion(self):
        print('Nada por aquí...')

    def limpiar_panel(self, panel):
        for widget in panel.winfo_children():
            widget.destroy()

    def abrir_panel_info(self):
        pass
 
    def esperando_login(self):
        self.frame_tapar = ctk.CTkFrame(self, fg_color='black')
        self.frame_tapar.pack(expand=True, fill='both')
        image_path = "./img/logo1.png"
        image_tapar = ctk.CTkImage(Image.open(image_path), size=(1024, 600))
        image_label = ctk.CTkLabel(self.frame_tapar, image=image_tapar, text='')
        image_label.place(x=0, y=0)
        btn_reabrir_login = ctk.CTkButton(self.frame_tapar, text='Iniciar Sesión', command=self.log_in, width=150, height=75)
        btn_reabrir_login.place(x=400, y=300)