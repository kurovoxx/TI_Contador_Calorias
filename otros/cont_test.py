import customtkinter as ctk
import time

class CircleBPMApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Medidor de Pulso")
        self.geometry("300x400")  # Aumentamos el alto para dar espacio a los nuevos elementos

        # Texto de instrucción arriba del todo con fuente Arial
        self.instruction_label = ctk.CTkLabel(self, text="Haga click para medir su pulso", font=("Arial", 12))
        self.instruction_label.pack(pady=10)  # Padding arriba

        # Contador de clicks que comenzará en 10
        self.counter = 10
        self.counter_label = ctk.CTkLabel(self, text=f"Contador: {self.counter}", font=("Arial", 16))
        self.counter_label.pack(pady=10)

        # Inicializamos variables para contar clics
        self.click_times = []
        self.timeout = 2.0  # 2 segundos de timeout para resetear las pulsaciones

        # Etiqueta para mostrar los BPM (colocada debajo del contador)
        self.bpm_label = ctk.CTkLabel(self, text="BPM: N/A")
        self.bpm_label.pack(pady=10)  # Se coloca después del contador

        # Creamos un botón circular con animación
        self.circle_button = ctk.CTkButton(self, text="", width=100, height=100, corner_radius=50, fg_color="blue", command=self.on_button_click)
        self.circle_button.pack(pady=50)  # Colocamos el botón más abajo para que todo quepa

        # Definimos los tamaños iniciales y mínimos
        self.original_size = 100
        self.shrinked_size = 50
        self.current_size = self.original_size

        # Velocidad de reducción
        self.shrink_speed = 2  # Cada ciclo reducirá en 2 píxeles el tamaño

        # Iniciar animación de reducción
        self.shrinking = True
        self.after(50, self.shrink_button)

    def shrink_button(self):
        """Función para reducir el tamaño del botón progresivamente."""
        if self.shrinking and self.current_size > self.shrinked_size:
            self.current_size -= self.shrink_speed
            self.circle_button.configure(width=self.current_size, height=self.current_size)
            self.after(50, self.shrink_button)  # Llamar de nuevo para continuar reduciendo

    def on_button_click(self):
        """Función que se ejecuta al hacer clic en el botón."""
        if self.counter > 0:
            self.counter -= 1  # Reducir el contador con cada clic
            self.counter_label.configure(text=f"Contador: {self.counter}")

            self.reset_button_size()  # Restaurar tamaño del botón
            self.record_click()       # Registrar el clic para calcular los BPM

    def reset_button_size(self):
        """Restaurar el tamaño original del botón."""
        self.shrinking = False  # Detenemos la animación de reducción
        self.current_size = self.original_size
        self.circle_button.configure(width=self.original_size, height=self.original_size)
        self.after(500, self.start_shrinking)  # Volver a iniciar la reducción después de 0.5 segundos

    def start_shrinking(self):
        """Reiniciar la animación de reducción."""
        self.shrinking = True
        self.after(50, self.shrink_button)

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

if __name__ == "__main__":
    app = CircleBPMApp()
    app.mainloop()
