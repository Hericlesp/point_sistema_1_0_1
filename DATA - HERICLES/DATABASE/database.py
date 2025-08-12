import sqlite3
import os

# Caminho do banco
DB_DIR = r"\\educcur03\Users\Public\Técnico Informática Noite\POINT - PROJETO\DATA - HERICLES\DATA"
DB_PATH = os.path.join(DB_DIR,"database.db")
 
# Criar ou conectar ao banco(arquivo para o POINT)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Criação de pasta, se n existir
if not os.path.exists(DB_DIR):
    os.makedirs(DB_DIR)

def criar_banco_e_tabelas():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    pass