from tkinter import PhotoImage
import customtkinter as ctk
from  janelas.cadastro_veiculo import CadastroVeiculo

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Aluga Car")
        self.geometry("1046x600")
        self.resizable(False, False)
        
        self.img_cad = PhotoImage(file="icons/car.png")
        self.img_exibir = PhotoImage(file="icons/exibir.png")
        self.img_alugar = PhotoImage(file="icons/rent.png")
        
        self.frame = ctk.CTkFrame(self, width=1046, height=150)
        self.frame.pack(fill="both", expand=False)
        
        self.frameBtns = ctk.CTkFrame(self, width=1046, height=300)
        self.frameBtns.pack(fill="both", expand=False)
        self.frameBtns.pack_propagate(False)
        
        self.fram3 = ctk.CTkFrame(self, width=1046, height=150)
        self.fram3.pack(fill="both", expand=False)
        
        self.btnCadastro = ctk.CTkButton(self.frameBtns, text="Cadastrar Veículo", 
                                         width=187, height=183, command=self.cadastro,
                                         image=self.img_cad, compound="top", fg_color='#363D50',
                                         font=('Open Sans', 16, 'bold'))
        self.btnCadastro.pack(side='left', expand=True)
        self.btnExibir = ctk.CTkButton(self.frameBtns, text="Visualizar Veículos", 
                                         width=187, height=183, command=self.cadastro,
                                         image=self.img_exibir, compound="top", fg_color='#363D50',
                                         font=('Open Sans', 16, 'bold'))
        self.btnExibir.pack(side='left', expand=True)
        self.btnExibir = ctk.CTkButton(self.frameBtns, text="Alugar Veículo", 
                                         width=187, height=183, command=self.cadastro,
                                         image=self.img_alugar, compound="top", fg_color='#363D50',
                                         font=('Open Sans', 16, 'bold'))
        self.btnExibir.pack(side='left', expand=True)

        
    
    def cadastro(self):
        janela_cadastro = CadastroVeiculo(self)
        janela_cadastro.grab_set()  

app = App()
app.mainloop()