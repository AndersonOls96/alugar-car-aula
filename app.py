import customtkinter as ctk
from tkinter import PhotoImage
from janelas.janela_cadastro import CadastroVeiculo
from janelas.janela_exibir import ExibirVeiculos
from janelas.janela_alugar import AlugarVeiculo

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Aluga Car")
        self.geometry("1046x600")
        self.resizable(False, False)
        self._set_appearance_mode('dark')

        self.img_cad = PhotoImage(file='icons/car.png')
        self.img_exibir = PhotoImage(file='icons/exibir.png')
        self.img_alugar = PhotoImage(file='icons/rent.png')

        self.frame1 = ctk.CTkFrame(self, width=1046, height=150, fg_color='#2F3448', corner_radius=0)
        self.frame1.pack(fill='both', expand=False)

        self.frameBtns = ctk.CTkFrame(self, width=1046, height=300, fg_color='#2F3448', corner_radius=0)
        self.frameBtns.pack(fill='both', expand=False)
        self.frameBtns.pack_propagate(False)

        self.frame2 = ctk.CTkFrame(self, width=1046, height=150, fg_color='#2F3448', corner_radius=0)
        self.frame2.pack(fill='both', expand=False)

        self.btnCadastro = ctk.CTkButton(self.frameBtns, text='Cadastrar Veículo', 
        width=187, height=183, image=self.img_cad, compound='top', fg_color="#363D50",
        font=('Open Sans', 16, 'bold'), command=self.cadastro)
        self.btnCadastro.pack(side = 'left', expand=True)

        self.btnExibir = ctk.CTkButton(self.frameBtns, text='Exibir Veículos',
        width=187, height=183, image=self.img_exibir, compound='top', fg_color='#363D50',
        font=('Open Sans', 16, 'bold'), command=self.exibir)
        self.btnExibir.pack(side='left', expand= True)

        self.btnAlugar = ctk.CTkButton(self.frameBtns, text='Alugar Veículo', 
        width=187, height=183, image=self.img_alugar, compound='top', fg_color='#363D50',
        font=('Open Sans', 16, 'bold'), command=self.alugar)
        self.btnAlugar.pack(side='left', expand=True)

    def cadastro(self):
        janela_cadastro = CadastroVeiculo(self)
        janela_cadastro.grab_set()

    def exibir(self):
        janela_exibir = ExibirVeiculos(self)
        janela_exibir.grab_set()
    
    def alugar(self):
        janela_alugar = AlugarVeiculo(self)
        janela_alugar.grab_set()


app = App()
app.mainloop()