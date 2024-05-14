import customtkinter as ctk

class ExibirVeiculos(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title('Visualização de Veículos')
        self.geometry('600x800')
        self.resizable(False, False)

        self.label_visualizar = ctk.CTkLabel(text="Janela Visualizar")
        self.label_visualizar.pack()
