import sqlite3
import os

DB_DIR = r"\\educcur03\Users\Public\Técnico Informática Noite\POINT - PROJETO\CASSIA - BACK\Henrique\data"
DB_PATH = os.path.join(DB_DIR, 'database.db')

def criar_banco_e_tabelas():
    # Abre a conexão dentro da função
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Criação da tabela usuarios
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            ID_USUARIO INTEGER PRIMARY KEY AUTOINCREMENT,
            NOME TEXT NOT NULL,
            CPF TEXT NOT NULL UNIQUE,
            RA TEXT NOT NULL UNIQUE,
            PERMISSAO TEXT NOT NULL CHECK(PERMISSAO IN ('ADMIN', 'ALUNO', 'PROFESSOR', 'ROOT'))
        )
    """)
    # PERMISSAO DA TABELA USUARIOS É A PRINCIPAL, ONDE A DE LOGIN VAI FAZER REFERENCIA A ELA

    # Criação da tabela login
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS login (
            ID_USER INTEGER PRIMARY KEY,
            CPF TEXT NOT NULL,
            RA TEXT NOT NULL,
            SENHA TEXT NOT NULL,
            PERMISSAO TEXT NOT NULL CHECK(PERMISSAO IN ('ADMIN', 'ALUNO', 'PROFESSOR', 'ROOT')),
            FOREIGN KEY (ID_USER) REFERENCES usuarios(ID_USUARIO)
        )
    """)
    # Inserindo usuários na tabela usuarios
    usuarios = [
        ('Hericles', '11111111111', 'RA0000', 'ROOT'),
        ('Maria Oliveira', '22222222222', 'RA0002', 'ALUNO'),
        ('Carlos Souza', '33333333333', 'RA0003', 'PROFESSOR'),
        ('Ana Santos', '44444444444', 'RA0004', 'ROOT'),
        ('Pedro Lima', '55555555555', 'RA0005', 'ADMIN'),
        ('Fernanda Costa', '66666666666', 'RA0006', 'ALUNO'),
        ('Lucas Almeida', '77777777777', 'RA0007', 'PROFESSOR'),
        ('Juliana Pereira', '88888888888', 'RA0008', 'ROOT'),
        ('Rafael Mendes', '99999999999', 'RA0009', 'ADMIN'),
        ('Camila Rocha', '10101010101', 'RA0010', 'ALUNO')
    ]
    for usuario in usuarios:
        cursor.execute("INSERT INTO usuarios (NOME, CPF, RA, PERMISSAO) VALUES (?, ?, ?, ?)", usuario)

    # Inserindo registros na tabela login
    logins = [
        (1, '11111111111', 'RA0000', 'senha123', 'ROOT'),
        (2, '22222222222', 'RA0002', 'senha123', 'ALUNO'),
        (3, '33333333333', 'RA0003', 'senha123', 'PROFESSOR'),
        (4, '44444444444', 'RA0004', 'senha123', 'ROOT'),
        (5, '55555555555', 'RA0005', 'senha123', 'ADMIN'),
        (6, '66666666666', 'RA0006', 'senha123', 'ALUNO'),
        (7, '77777777777', 'RA0007', 'senha123', 'PROFESSOR'),
        (8, '88888888888', 'RA0008', 'senha123', 'ROOT'),
        (9, '99999999999', 'RA0009', 'senha123', 'ADMIN'),
        (10, '10101010101', 'RA0010', 'senha123', 'ALUNO')
    ]
    for login in logins:
        cursor.execute("INSERT INTO login (ID_USER, CPF, RA, SENHA, PERMISSAO) VALUES (?, ?, ?, ?, ?)", login)

    conn.commit()
    conn.close()
    
    
if __name__ == "__main__":
    criar_banco_e_tabelas()
    print("Tabelas criadas com sucesso ✅")
    # tabelasadd()
    # print("Dados inseridos com sucesso 🔢")
    

# #NECESSIDADES PARA A PAGINA DE LOGIN
# '''
# LOGIN 
#    *CPF OU RA
# SENHA
#     *PRIMEIRA SENHA CPF
#     TROCAR NO PRIMEIRO ACESSO
#     *SENHA PADRÃO RA
#     *SENHA PADRÃO CPF
# PERMISSAOES
#     *ADMINISTRADOR
#     *ALUNO
#     *PROFESSOR
#     *ROOT

# '''