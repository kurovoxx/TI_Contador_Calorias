from PIL import ImageTk, Image
import customtkinter as ctk
import os


def leer_imagen(path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.Resampling.LANCZOS))


def cargar_imagenes_para_ctkbutton(carpeta="img"):
    imagenes = []

    # Obtener todos los archivos .png de la carpeta especificada
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".png"):
            ruta_imagen = os.path.join(carpeta, archivo)

                # Cargar la imagen con PIL
            imagen = Image.open(ruta_imagen).resize((100, 100))

                # Convertir la imagen al formato CTkImage
            ctk_imagen = ctk.CTkImage(imagen)

                # Agregar la imagen convertida a la lista
            imagenes.append(ctk_imagen)

    return imagenes

        

        