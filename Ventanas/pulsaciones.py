import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from util.colores import *
import time


class Pulsaciones(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('400x400')
        self.title('Medidor de Pulso')
        self.attributes('-topmost', True)
        self.resizable(False, False)

        self.counter = 10
        self.click_times = []
        self.timeout = 2.0  # 2 segundos de timeout para resetear las pulsaciones

        self.main_frame = ctk.CTkFrame(self, fg_color=gris)
        self.main_frame.pack(fill='both', expand=True)

        self.add_widget()

    def add_widget(self):
        self.instruction_label = ctk.CTkLabel(self.main_frame, text="Haga click para medir su pulso", text_color="white", font=("Arial", 20), 
                                          width=200)
        self.instruction_label.pack(pady=(20, 10))

        # Contador de clicks que comenzará en 10
        self.counter_label = ctk.CTkLabel(self.main_frame, text=f"Contador: {self.counter}", font=("Arial", 20, 'bold'), bg_color=azul_medio_oscuro)
        self.counter_label.configure(corner_radius=20)
        self.counter_label.pack(pady=10)

        # Etiqueta para mostrar los BPM
        self.bpm_label = ctk.CTkLabel(self.main_frame, text="BPM: N/A", font=("Arial", 20, 'bold'), bg_color=azul_medio_oscuro)
        self.bpm_label.configure(corner_radius=20)
        self.bpm_label.pack(pady=10)

        # Botón circular
        self.circle_button = ctk.CTkButton(self.main_frame, text="", width=100, height=100, corner_radius=50, fg_color=verde_boton, command=self.on_button_click, hover_color=verde_oscuro)
        self.circle_button.pack(pady=50)

    def on_button_click(self):
        """Función que se ejecuta al hacer clic en el botón."""
        if self.counter > 0:
            self.counter -= 1  # Reducir el contador con cada clic
            self.counter_label.configure(text=f"Contador: {self.counter}")
            self.record_click()  # Registrar el clic para calcular los BPM

            # Si el contador llega a 0, mostrar los resultados
            if self.counter == 0:
                self.show_final_message()

    def record_click(self):
        """Función para registrar los tiempos de clic y calcular los BPM."""
        current_time = time.time()

        # Verificar si hay un timeout (si pasó mucho tiempo desde el último clic)
        if self.click_times and current_time - self.click_times[-1] > self.timeout:
            self.click_times.clear()  # Reiniciar los tiempos si el tiempo entre clics es mayor al timeout

        # Registrar el clic actual
        self.click_times.append(current_time)

        # Calcular BPM si hay más de un clic
        if len(self.click_times) > 1:
            # Mantener solo los últimos 4 clics
            if len(self.click_times) > 4:
                self.click_times.pop(0)

            # Calcular el intervalo de tiempo entre el primer y último clic
            time_interval = self.click_times[-1] - self.click_times[0]
            clicks = len(self.click_times)

            # Calcular BPM (Beats Per Minute)
            if time_interval > 0:
                bpm = (clicks - 1) * 60 / time_interval
                self.bpm_label.configure(text=f"BPM: {int(bpm)}")

    def show_final_message(self):
        """Mostrar el resultado final con el número de pulsaciones y la intensidad del entrenamiento."""
        if self.click_times:
            # Calcular el BPM final basándonos en los últimos clics registrados
            time_interval = self.click_times[-1] - self.click_times[0]
            clicks = len(self.click_times)
            if time_interval > 0:
                bpm = (clicks - 1) * 60 / time_interval
                bpm = int(bpm)  # Asegurarnos de que el valor sea un número entero

                # Determinar la intensidad del entrenamiento según el BPM
                if bpm < 100:
                    message = f"Pulsaciones finales: {bpm}\nIntenta aumentar la intensidad de tu entrenamiento."
                elif 100 <= bpm <= 120:
                    message = f"Pulsaciones finales: {bpm}\nIntensidad: ligera."
                elif 121 <= bpm <= 140:
                    message = f"Pulsaciones finales: {bpm}\nIntensidad: moderada."
                else:
                    message = f"Pulsaciones finales: {bpm}\nIntensidad alta."

                # Cerrar la ventana actual
                self.destroy()

                # Mostrar el resultado en un CTkMessagebox
                CTkMessagebox(title="Resultado del Entrenamiento", message=message, icon="check", option_1="Ok")
