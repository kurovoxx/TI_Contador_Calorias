import customtkinter as ctk
import time

# Inicializamos la app
app = ctk.CTk()
app.geometry("300x200")

# Creamos una barra de progreso
progress_bar = ctk.CTkProgressBar(app, width=200, height=20)
progress_bar.place(relx=0.5, rely=0.5, anchor="center")

# Establecemos el valor de la barra de progreso (0.0 - 1.0)
progress_bar.set(0)

# Función para incrementar el progreso
def update_progress():
    for i in range(101):
        progress_bar.set(i / 100)
        app.update()
        time.sleep(0.05)

# Botón para iniciar el progreso
start_button = ctk.CTkButton(app, text="Iniciar", command=update_progress)
start_button.place(relx=0.5, rely=0.7, anchor="center")

# Iniciamos el loop principal de la app
app.mainloop()
