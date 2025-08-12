
import tkinter as tk
from tkinter import ttk
# import Pagina_de_Funcoes as Pf

class POINT:
    def __init__(self,janela):
        self.janela=janela
        self.janela.title("POINT")
        self.janela.geometry("450x500")

        self.tarefas = []

        self.style = ttk.Style()
        #self.style.configure(bg="l")
        # self.style.theme_use("")
        self.criar_widgets()


    def criar_widgets(self):

        frame_up = tk.Frame(self.janela)
        frame_up.pack(fill="x")

        frame_principal = tk.Frame(self.janela, pady=20)
        frame_principal.pack()

        frame_donw = tk.Frame(self.janela)
        frame_donw.pack( )




        login =tk.Label(frame_principal, text="LOGIN",font=("arial",16))
        login.grid(row=1, column=2, padx=5, pady=5)

        self.entrada_tarefa = tk.Entry(frame_principal, width=50)
        self.entrada_tarefa.grid(row=2, column=2, padx=5, pady=5)
        self.entrada_tarefa.focus()

        senha = tk.Label(frame_principal, text="SENHA",font=("arial",16))
        senha.grid(row=3, column=2, padx=5, pady=5)
        
        self.entrada_tarefa = tk.Entry(frame_principal, width=50)
        self.entrada_tarefa.grid(row=4, column=2, padx=5, pady=5)
        self.entrada_tarefa.focus()

        botao_login = tk.Button(frame_principal, text="Login",width=30,)
        botao_login.grid(row=5, column=2,padx=2,pady=1)
        
        



if __name__== "__main__":
    janela = tk.Tk()
    app= POINT(janela)
    janela.mainloop()
    

