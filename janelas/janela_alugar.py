import customtkinter as ctk

class AlugarVeiculo(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Alugar Veículo")
        self.geometry('800x600')
        self.resizable(False, False)

        self.texto = ctk.CTkLabel(self, text="Janela Alugar")
        self.texto.pack()