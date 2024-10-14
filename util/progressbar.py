import customtkinter as ctk
import tkinter as tk

calorias_diarias = 0

def actualizar_barra(calorias, calorias_objetivo):
    progreso = calorias / calorias_objetivo
    barra.set(progreso)

    if progreso <= 0.5:
        barra.configure(progress_color="red")
    elif progreso <= 0.75:
        barra.configure(progress_color="yellow")
    else:
        barra.configure(progress_color="green")

def ingresar_calorias():
    global calorias_diarias
    calorias_nuevas = float(entrada_calorias.get()) 
    calorias_diarias += calorias_nuevas 
    calorias_objetivo = float(entrada_objetivo.get())

    actualizar_barra(calorias_diarias, calorias_objetivo)

    label_total_calorias.configure(text=f"Total calorías del día: {calorias_diarias}")

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
ventana = ctk.CTk()
ventana.title("Barra de Progreso de Calorías Diarias")
ventana.geometry("400x350")

label_calorias = ctk.CTkLabel(ventana, text="Añadir calorías:")
label_calorias.pack(pady=10)
entrada_calorias = ctk.CTkEntry(ventana, width=200)
entrada_calorias.pack(pady=5)

label_objetivo = ctk.CTkLabel(ventana, text="Calorías objetivo del día:")
label_objetivo.pack(pady=10)
entrada_objetivo = ctk.CTkEntry(ventana, width=200)
entrada_objetivo.pack(pady=5)

boton = ctk.CTkButton(ventana, text="Añadir Calorías del Día", command=ingresar_calorias)
boton.pack(pady=20)

label_total_calorias = ctk.CTkLabel(ventana, text="Total calorías del día: 0")
label_total_calorias.pack(pady=10)

barra = ctk.CTkProgressBar(ventana, width=300)
barra.pack(pady=20)
barra.set(0)
barra.configure(progress_color="red") 

ventana.mainloop()
