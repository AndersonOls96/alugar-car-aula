import customtkinter as ctk

class CadastroVeiculo(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Cadastro de Veículos")
        self.geometry("800x600")
        self.resizable(False, False)

        self.label_exemplo = ctk.CTkLabel(self, text='Exemplo')
        self.label_exemplo.pack()
