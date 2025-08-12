
import tkinter as tk
from tkinter import ttk


class POINT:
    def __init__(self,janela):
        self.janela=janela
        self.janela.title("Gerenciador de Tarefas")
        self.janela.geometry("800x600")

        self.tarefas = []

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.criar_widgets()


    def criar_widgets(self):
        frame_principal = ttk.Frame(self.janela , padding="10")
        frame_principal.pack(fill= tk.BOTH, expand=True)

        Entrada_frame = ttk.Frame(frame_principal,padding=10)
        Entrada_frame.pack()

        ttk.Label(Entrada_frame, text="LOGIN:").grid(row=3, column=2, padx=5, pady=5)
        self.entrada_tarefa = ttk.Entry(Entrada_frame, width=50)
        self.entrada_tarefa.grid(row=2, column=2, padx=5, pady=5)
        self.entrada_tarefa.focus()

        ttk.Label(Entrada_frame, text="SENHA:").grid(row=3, column=2, padx=5, pady=5)
        self.entrada_tarefa = ttk.Entry(Entrada_frame, width=50)
        self.entrada_tarefa.grid(row=4, column=2, padx=5, pady=5)
        self.entrada_tarefa.focus()

        botao_login = ttk.Button(Entrada_frame, text="Login")
        botao_login.grid(row=5, column=2,padx=2,pady=1)

        botao_cadastro= ttk.Button(Entrada_frame, text="Cadastro")
        botao_cadastro.grid(row=8,column=2,padx=2,pady=1)


    # def botao_login(self):
        

    # def botao_cadastro(self):


janela=tk.Tk()
app = POINT(janela)
janela.mainloop()







# if __name__== "__main__":
#     janela = tk.Tk()
#     app= POINT(janela)
#     janela.mainloop()
    

