import customtkinter as ctk

class CadastroVeiculo(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Cadastro de Veículo")
        self.geometry("800x600")  # Ajuste conforme necessário
        self.resizable(False, False)

        self.label_exemplo = ctk.CTkLabel(self, text="Cadastro de veículo", font=('Open Sans', 20, 'bold'))
        self.label_exemplo.pack(pady=10)
        
        self.label_marca = ctk.CTkLabel(self, text="Marca:", font=('Open Sans', 16, 'bold'))
        self.label_marca.pack(pady=5)
        
        self.entry_marca = ctk.CTkEntry(self, font=('Open Sans', 16, 'bold'))
        self.entry_marca.pack(pady=5)
        
        self.label_modelo = ctk.CTkLabel(self, text="Modelo:")
        self.label_modelo.pack(pady=5)
        
        self.entry_modelo = ctk.CTkEntry(self)
        self.entry_modelo.pack(pady=5)
        
        self.label_ano = ctk.CTkLabel(self, text="Ano:")
        self.label_ano.pack(pady=5)
        
        self.entry_ano = ctk.CTkEntry(self)
        self.entry_ano.pack(pady=5)
        
        self.btn_cadastrar = ctk.CTkButton(self, text="Cadastrar", command=self.cadastrar)
        self.btn_cadastrar.pack(pady=10)
        
    def cadastrar(self):
        marca = self.entry_marca.get()
        modelo = self.entry_modelo.get()
        ano = self.entry_ano.get()
        
        print(f'Marca: {marca}, Modelo: {modelo}, Ano: {ano}')
        self.destroy()
        
        

        