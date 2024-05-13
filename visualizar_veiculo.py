import customtkinter as ctk

class VisualizarVeiculo(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Cadastro de Veículo")
        self.geometry("400x300")  # Ajuste conforme necessário
        self.resizable(False, False)

        self.label_exemplo = ctk.CTkLabel(self, text="Exemplo de Label")
        self.label_exemplo.pack(pady=10)

        