import customtkinter as ctk

class ExibirVeiculos(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title('Visualização de Veículos')
        self.geometry('800x600')
        self.resizable(False, False)

        self.frameTitulo = ctk.CTkFrame(self, width=800, height=100, corner_radius=0)
        self.frameTitulo.pack(fill='both', expand=False)
        self.frameTitulo.pack_propagate(False)

        self.frameTabela = ctk.CTkFrame(self, width=800, height=500, corner_radius=0)
        self.frameTabela.pack(fill='both', expand=False)
        self.frameTabela.pack_propagate(False)

        self.labelTitulo = ctk.CTkLabel(self.frameTitulo, text='Visualizar Veículos', 
        font=('Open Sans', 26, 'bold'), text_color='white')
        self.labelTitulo.pack(side='bottom')
