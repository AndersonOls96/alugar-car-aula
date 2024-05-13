import sqlite3

def criar_banco_de_dados():
    conexao = sqlite3.connect('locadora.db')
    cursor = conexao.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS veiculo (
        id INTEGER PRIMARY KEY,
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL,
        ano INTEGER NOT NULL,
        alugado BOOLEAN NOT NULL CHECK (alugado IN (0, 1)),
        tipo TEXT NOT NULL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS carro (
        veiculo_id INTEGER PRIMARY KEY,
        portas INTEGER NOT NULL,
        FOREIGN KEY(veiculo_id) REFERENCES veiculo(id)
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS motocicleta (
        veiculo_id INTEGER PRIMARY KEY,
        cilindradas INTEGER NOT NULL,
        FOREIGN KEY(veiculo_id) REFERENCES veiculo(id)
    )
    ''')
    
    conexao.commit()
    conexao.close()