import customtkinter as ctk
from PIL import Image, ImageDraw, ImageTk

def rec_bg(root, width, height, radius, color):
    # Crear un canvas con el mismo tamaño que el rectángulo
    canvas = ctk.CTkCanvas(root, width=width, height=height)
    
    # Crear una imagen con fondo transparente (RGBA)
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))  # Fondo transparente
    draw = ImageDraw.Draw(image)

    # Dibujar el rectángulo redondeado
    draw.rounded_rectangle((0, 0, width, height), radius=radius, fill=color)

    # Convertir la imagen a un formato que tkinter pueda usar
    tk_image = ImageTk.PhotoImage(image)

    # Mostrar la imagen en el canvas
    canvas.create_image(width // 2, height // 2, image=tk_image)

    # Asignar la imagen al root para evitar que sea recolectada por el garbage collector
    root.tk_image = tk_image  # Guardamos la referencia en el widget root

    return canvas

def main():
    # Inicializar customtkinter
    ctk.set_appearance_mode("light")  # Puede ser "dark" o "light"
    ctk.set_default_color_theme("blue")  # Cambiar el tema de colores si se desea

    # Crear la ventana principal con customtkinter
    root = ctk.CTk()
    root.title("Rectángulo Redondeado con customtkinter y PIL")

    # Crear un rectángulo redondeado (esto creará el canvas internamente)
    rounded_rect_canvas = create_rounded_rectangle(root, width=200, height=100, radius=30, color="blue")
    
    # Colocar el canvas en la ventana
    rounded_rect_canvas.pack(pady=20)

    # Añadir una etiqueta encima usando CTkLabel
    label = ctk.CTkLabel(root, text="Mi Rectángulo Redondeado")
    label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
