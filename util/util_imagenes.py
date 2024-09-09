from PIL import ImageTk, Image
import customtkinter as ctk
import os


def leer_imagen(path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.Resampling.LANCZOS))


def cargar_imagenes(carpeta: str) -> list[ctk.CTkImage]:
    imagenes = []

    for archivo in os.listdir(carpeta):
        if archivo.endswith(".png"):
            ruta_imagen = os.path.join(carpeta, archivo)

            imagen = Image.open(ruta_imagen).resize((100, 100))

            ctk_imagen = ctk.CTkImage(imagen)

            imagenes.append(ctk_imagen)
    return imagenes

def cargar_imagen(file: str, w: int=100, h: int=100) -> ctk.CTkImage:
    imagen = Image.open(file)
    
    imagen = imagen.resize((w, h))  # Las dimensiones deben ser una tupla
    
    ctk_image = ctk.CTkImage(imagen)
    
    return ctk_image
