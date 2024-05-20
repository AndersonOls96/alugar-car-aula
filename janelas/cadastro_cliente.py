import customtkinter as ctk
from db.database import Database

class CadastroCliente(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Cadastro de Veículos")
        self.geometry("800x600")
        self.resizable(False, False)
        
        self.frameTitulo = ctk.CTkFrame(self, width=800, height=100, corner_radius= 0)
        self.frameTitulo.pack(fill='both', expand=False)
        self.frameTitulo.pack_propagate(False)

        self.frameItens = ctk.CTkFrame(self, width=800, height=500, corner_radius=0)
        self.frameItens.pack(fill='both', expand=False)
        self.frameItens.pack_propagate(False)

        self.labelTitulo = ctk.CTkLabel(self.frameTitulo, text='Cadastrar Cliente', 
        font=('Open Sans', 26, 'bold'), text_color='white')
        self.labelTitulo.pack(side='bottom')

        self.labelNome = ctk.CTkLabel(self.frameItens, text='Nome', font=('Open Sans', 16))
        self.labelNome.pack(pady=10)
        self.entryNome = ctk.CTkEntry(self.frameItens, font=('Open Sans', 16))
        self.entryNome.pack(pady=5)

        self.labelTelefone = ctk.CTkLabel(self.frameItens, text='Telefone', font=('Open Sans', 16))
        self.labelTelefone.pack(pady=10)
        self.entryTelefone = ctk.CTkEntry(self.frameItens, font=('Open Sans', 16))
        self.entryTelefone.pack(pady=5)

        self.labelCPF = ctk.CTkLabel(self.frameItens, text='CPF', font=('Open Sans', 16))
        self.labelCPF.pack(pady=10)
        self.entryCPF = ctk.CTkEntry(self.frameItens, font=('Open Sans', 16))
        self.entryCPF.pack(pady=5)

        self.labeEmail = ctk.CTkLabel(self.frameItens, text='Email', font=('Open Sans', 16))
        self.labeEmail.pack(pady=10)
        self.entryEmail = ctk.CTkEntry(self.frameItens, font=('Open Sans', 16))
        self.entryEmail.pack(pady=5)

        self.btnCadastrar = ctk.CTkButton(self.frameItens, text='Cadastrar', font=('Open Sans', 16), command=self.cadastrar_cliente)
        self.btnCadastrar.pack(pady=30)

    def cadastrar_cliente(self):
        cpf = self.entryCPF.get()
        nome = self.entryNome.get()
        telefone = self.entryTelefone.get()
        email = self.entryEmail.get()
        
        if cpf and nome and telefone and email:
            db = Database("db/locadora.db")
            db.connect()
            query = f"INSERT INTO clientes (cpf, nome, telefone, email) VALUES ('{cpf}', '{nome}', '{telefone}', '{email}')"
            msg_ok = "Cliente cadastrado com sucesso."
            msg_error = "Erro ao cadastrar cliente."
            db.execute_query(query, msg_ok, msg_error)
            self.entryCPF.delete(0, 'end')
            self.entryNome.delete(0, 'end')
            self.entryTelefone.delete(0, 'end')
            self.entryEmail.delete(0, 'end')
            db.disconnect()