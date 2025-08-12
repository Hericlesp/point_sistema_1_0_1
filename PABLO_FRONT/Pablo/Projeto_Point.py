from tkinter import messagebox
import tkinter as tk   
from tkinter import ttk

class Point:
    def __init__(self,janela):
        self.janela=janela
        self.janela.title("Area do Aluno")
        self.janela.geometry("300x450")
        self.janela.tk_setPalette(background="green")
        self.tarefas = []

        # Configuração do tema
           
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.criar_widgets()

    def criar_widgets(self):
        
        
        #Frame de Entrada

        up_frame = tk.Frame(self.janela)
        up_frame.pack()

        #Frame Principal

        frame_principal = tk.Frame(self.janela)
        frame_principal.pack()

        down_frame = tk.Frame(self.janela)
        down_frame.pack()


        
        # Labels Nome do Aluno e Descrição do Curso
        self.descricao_curso = tk.Label(up_frame, text="Tecnico de Internet", font=("Arial", 16, "bold"), bg="#690E0E", fg="white")
        self.descricao_curso.grid(row=0, column=1, padx=50, pady=5)

        self.nome_aluno = tk.Label(up_frame, text="Nome do Aluno", font=("Arial", 14), bg="#690E0E", fg="white")
        self.nome_aluno.grid(row=1, column=1, padx=50)
        
        self.matricula = tk.Label(up_frame,text=(f"MATRICULA:{"matricula"}"), font=("Arial", 10), bg="#690E0E", fg="white")
        self.matricula.grid(row=2, column=1, padx=50)
        



        #Labels e Botões para Marcar Frequência
        
        self.entrada_frequencia = tk.Label(frame_principal, text="Primeiro horário", font=("Arial", 12), bg="#690E0E", fg="white")
        self.entrada_frequencia.grid(row=2, column=1, padx=50, pady=20)
        self.entrada_frequencia = tk.Button(frame_principal,text="Marcar Frequência", width=20)
        self.entrada_frequencia.grid(row=3, column=1, padx=50, pady=5)
        self.entrada_frequencia.focus()

        self.entrada_frequencia = tk.Label(frame_principal, text="Segundo horário", font=("Arial", 12), bg="#690E0E", fg="white")
        self.entrada_frequencia.grid(row=4, column=1, padx=80, pady=20)
        self.entrada_frequencia2= tk.Button(frame_principal, text="Marcar Frequência", width=20)
        self.entrada_frequencia2.grid(row=5, column=1, padx=80, pady=5)

        self.entrada_frequencia = tk.Label(frame_principal, text="Terceiro horário", font=("Arial", 12), bg="#690E0E", fg="white")
        self.entrada_frequencia.grid(row=6, column=1, padx=80, pady=20)
        self.entrada_frequencia3= tk.Button(frame_principal, text="Marcar Frequência", width=20)
        self.entrada_frequencia3.grid(row=7, column=1, padx=80, pady=5)

        

       



janela= tk.Tk()
app = Point(janela)
janela.mainloop()


    