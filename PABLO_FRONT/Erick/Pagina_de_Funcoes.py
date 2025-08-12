import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

# 🔗 Caminho do banco
DB_DIR = r"\\educcur03\Users\Public\Técnico Informática Noite\POINT - PROJETO\CASSIA_BACK\Henrique\data"
DB_PATH = os.path.join(DB_DIR, 'database.db')


class Valida_logi:
    
    def __init__(self,login,senha):
        self.login = login
        self.senha = senha
    
    def valida_login(self,login,senha):
        if login == ("RA" or "CPF") and senha == "SENHA":
            return True
        
        
        
        
    #-----------------------
    def fazer_login(self):
        matricula = self.usuario_var.get().strip()
        senha = self.senha_var.get().strip()

        if not matricula or not senha:
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
            return
        
        try:
            matricula_int = int(matricula)  # Convertendo para inteiro
            
        except ValueError:
            messagebox.showerror("Erro", "Matrícula deve ser numérica.")
            return

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT cargo FROM Usuarios WHERE matricula = ? AND senha = ?",
            (matricula_int, senha)
        )
        resultado = cursor.fetchone()
        conn.close()

    
        if resultado:
            cargo = resultado[0]
            messagebox.showinfo("Login", f"Bem-vindo, {cargo.upper()}!")

            self.root.destroy()  # Fecha a janela de login

               
            if cargo in ["ROOT", "ADM"]:
                novo_root = tk.Tk()
                main.SistemaPonto(novo_root).run()

                
            elif cargo == "USER":
                novo_root = tk.Tk()
                USER_ponto_user_main.SistemaPonto(novo_root, matricula_int).run()

            else:
                messagebox.showerror("Erro", "Permissão desconhecida!")

        else:
            messagebox.showerror("Erro", "Matrícula ou senha incorretos.")
