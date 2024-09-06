import customtkinter as ctk

class Log_in(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry('500x600')
        self.title('Log In')
        self.resizable(False, False)
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill='both', expand=True)
        self.add_widget_login()

    def add_widget_login(self):
        self.limpiar_panel()

        self.frame = ctk.CTkFrame(self.main_frame, fg_color='red')
        self.frame.pack(fill='both', expand=True)

        self.btn_iniciar = ctk.CTkButton(self.frame, text='Iniciar Sesión', width=170, height=50, command=self.win_iniciar)
        self.btn_iniciar.place(x= 170, y=100)

        self.btn_registrarse = ctk.CTkButton(self.frame, text='Registrarse', width=170, height=50, command=self.win_registrar)
        self.btn_registrarse.place(x=170, y=180)
    
    def win_iniciar(self):
        self.limpiar_panel()

        self.frame_iniciar = ctk.CTkFrame(self.main_frame, fg_color='blue')
        self.frame_iniciar.pack(fill='both', expand=True)

        self.btn_volver = ctk.CTkButton(self.frame_iniciar, text='Volver Atrás', command=self.add_widget_login)
        self.btn_volver.place(x=180, y=300)
    
    def win_registrar(self):
        self.limpiar_panel()

        self.frame_registrar = ctk.CTkFrame(self.main_frame, fg_color='yellow')
        self.frame_registrar.pack(fill='both', expand=True)

        self.btn_volver = ctk.CTkButton(self.frame_registrar, text='Volver Atrás', command=self.add_widget_login)
        self.btn_volver.place(x=180, y=300)

    def limpiar_panel(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()