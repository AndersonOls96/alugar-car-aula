import sqlite3
from tkinter import messagebox

class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_file)
            print("Conexão com o banco de dados estabelecida.")
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Conexão com o banco de dados encerrada.")
            
    def create_table(self, table_name, columns):
        try:
            query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print(f"Tabela {table_name} criada com sucesso.")
        except Exception as e:
            print(f"Erro ao criar a tabela {table_name}: {e}")
    
    def execute_query(self, query, msg_ok, msg_error):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Query executada com sucesso.")
            messagebox.showinfo("Sucesso", msg_ok)
        except sqlite3.Error as e:
            print(f"Erro ao executar a query: {e}")
            messagebox.showerror("Erro", msg_error)

# Exemplo de uso
db = Database("db/veiculos.db")
db.connect()
db.create_table("veiculos", ["placa TEXT PRIMARY KEY", "marca TEXT", "modelo TEXT", "ano INTEGER", "disponibilidade TEXT DEFAULT 'Disponível'"])
db.disconnect()