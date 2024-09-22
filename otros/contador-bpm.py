import customtkinter as ctk
import time

class BPMApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("BPM Detector")
        self.geometry("300x200")

        self.click_times = []
        self.bpm_label = ctk.CTkLabel(self, text="BPM: N/A")
        self.bpm_label.pack(pady=20)

        self.click_button = ctk.CTkButton(self, text="Click me", command=self.record_click)
        self.click_button.pack(pady=20)

    def record_click(self):
        current_time = time.time()
        self.click_times.append(current_time)

        # Solo calcular si hay más de 1 clic
        if len(self.click_times) > 1:
            # Tomar los tiempos de los últimos 4 clics
            if len(self.click_times) > 4:
                self.click_times.pop(0)

            # Calcular el intervalo de tiempo entre el primer y el último clic
            time_interval = self.click_times[-1] - self.click_times[0]
            clicks = len(self.click_times)
            
            # Calcular BPM
            bpm = (clicks - 1) * 60 / time_interval
            self.bpm_label.configure(text=f"BPM: {int(bpm)}")

if __name__ == "__main__":
    app = BPMApp()
    app.mainloop()
