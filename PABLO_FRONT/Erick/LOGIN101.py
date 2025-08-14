
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import os

import sys
sys.path.append(r"\\educcur03\Users\Public\Técnico Informática Noite\point_sistema_1_0_1")

from PABLO_FRONT.Pablo.Projeto_Point import Point
import PABLO_FRONT.Deyu.adm_aparencer_professor as adm

#import Pagina_de_Funcoes as Pf

#CAMINHO DO BANCO


DB_DIR = r"\\educcur03\Users\Public\Técnico Informática Noite\point_sistema_1_0_1\CASSIA_BACK\Henrique\data"
DB_PATH = os.path.join(DB_DIR, 'database.db')

sys.path.append(r"\\educcur03\Users\Public\Técnico Informática Noite\point_sistema_1_0_1")


class POINT:
  def __init__(self,janela):
    self.janela=janela
    self.janela.title("POINT")
    self.janela.geometry("450x420")
    self.janela.configure(bg="#E2E2E2")

    self.var_usuario = tk.StringVar()
    self.var_senha = tk.StringVar()
    

    self.style = ttk.Style()
    #self.style.configure(bg="l")
    # self.style.theme_use("")
    self.criar_widgets()
    
    
    


  def criar_widgets(self):

    frame_up = tk.Frame(self.janela, bg="#002CA7",)
    frame_up.pack(fill="x")

    frame_principal = tk.Frame(self.janela,bg="#E2E2E2")
    frame_principal.pack(fill="both", expand=True, padx=20, pady=8)
    #frame_principal.pack_propagate(False)  # Impede que o frame encolha para caber no conteúdo

    frame_donw = tk.Frame(self.janela, bg="#002CA7", height=200)
    frame_donw.pack(fill="x", pady=15)

      # _____________ TITULO_____________
    intro =tk.Label(frame_up, text=("POINT"),fg="#E2E2E2", bg="#002CA7",font=("arial",30,"italic","bold"))
    intro.pack( padx=5, pady=5)
    intro_sub =tk.Label(frame_up, text=("Ponto Digital"),fg="#E2E2E2", bg="#002CA7",font=("arial",30,"italic","bold"))
    intro_sub.pack( padx=10 )
      # _____________ LOGIN_____________
    login =tk.Label(frame_principal, text="LOGIN",font=("arial",16,"bold"))
    login.config( bg="#E2E2E2")
    login.pack( padx=5, pady=5)

    self.entrada_usuario = tk.Entry(frame_principal, textvariable=self.var_usuario, font=("arial", 16), width=50)
    self.entrada_usuario.pack( padx=5, pady=5)
    self.entrada_usuario.focus()

    senha = tk.Label(frame_principal, text="SENHA",font=("arial",16,"bold"))
    senha.config( bg="#E2E2E2")
    senha.pack( padx=5, pady=5)
    
    self.entrada_senha = tk.Entry(frame_principal, textvariable=self.var_senha, show="*", font=("arial", 16), width=50)
    self.entrada_senha.pack( padx=5, pady=5)
    

    botao_login = tk.Button(frame_principal, text="LOGIN", font=("arial",16,"bold") ,width=20,command=self.fazer_login)
    botao_login.pack(padx=2,pady=5)
    
      # _____________ FOOTER_____________        
    footer =tk.Label(frame_donw, text=("@ todos direitos reservados"),fg="white", bg="#002CA7",font=("arial",12,"italic"))
    footer.pack( padx=5)

    footer2 =tk.Label(frame_donw, text=("TEC. INTERNET - SERVENTE D' SOFTWARE"),fg="white", bg="#002CA7",font=("arial",10,"italic"))
    footer2.pack( padx=10)  
    
  def fazer_login(self):
    usuario =self.var_usuario.get().strip().upper()
    senha = self.var_senha.get().strip().upper()

    #validação inicial    
    if not usuario or not senha:
      messagebox.showwarning("ATENÇÃO"," Preencha todos os campos")
      return
    
    try:
      usuario_int = int(usuario)
      
    except ValueError:
      messagebox.showerror("ERRO"," Usuario ou senha incorreto")
      return
    
    
    #conecta ao banco para extrair os dados
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
  
    cursor.execute(
    "SELECT NOME,PERMISSAO FROM login WHERE (CPF = ? OR RA = ?) AND SENHA = ? ",(usuario_int,usuario_int, senha)
    )
  
    resultado = cursor.fetchone()
    conn.commit()


    #valida entrada
    if resultado:
      
      user = resultado[1]
      user_name = resultado[0]
      
      messagebox.showinfo("Login",f"Bem-Vindo, {user_name.upper()}!")
      
      self.janela.destroy()
      
      if user in ("ROOT", "PROFESSOR"):
        new_janela = tk.Tk()
        Point(new_janela).run()
        
      elif user == "aluno":
        new_janela = tk.Tk()
        adm.Inicial(new_janela,usuario_int).run()
      
      else:
        messagebox.showerror("ERRO", " Permissão desconhecida")
    
    else:
      messagebox.showerror("ERRO!"," Matrícula ou senha incorreos.")
      
    


if __name__== "__main__":
    janela = tk.Tk()
    app= POINT(janela)
    janela.mainloop()
    

