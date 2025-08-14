from tkinter import messagebox
import tkinter as tk   
from tkinter import ttk

class Point:
    def __init__(self,janela):
        self.janela=janela
        self.janela.title("Area do Aluno")
        self.janela.geometry("450x350")
        self.janela.tk_setPalette(background="#E2E2E2")
        self.tarefas = []

        # Configuração do tema
           
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.criar_widgets()

    def criar_widgets(self):
        
        
        #Frame de Entrada
    


        up_frame = tk.Frame(self.janela, background="#002CA7")
        up_frame.pack(fill="x", pady=15)
        
        up_frame_config = tk.Frame(up_frame, background="#002CA7")
        up_frame_config.grid(column=0, padx=15)

        #Frame Principal

        frame_principal = tk.Frame(self.janela, background="#E2E2E2")
        frame_principal.pack()

        down_frame = tk.Frame(self.janela, background="#002CA7")
        down_frame.pack()


        
        # Labels Nome do Aluno e Descrição do Curso
        
        
    
        self.descricao_curso = tk.Label(up_frame, text="Tecnico de Internet", font=("Arial", 22, "bold"), bg="#002CA7",fg="#e2e2e2")
        self.descricao_curso.grid(row=0, column=1, pady=15)

        self.nome_aluno = tk.Label(up_frame, text="Nome do Aluno", font=("Arial", 18), bg="#002CA7", fg="#e2e2e2")
        self.nome_aluno.grid(row=2, column=1, padx=50)
        
        self.matricula = tk.Label(up_frame,text=(f"MATRICULA:{"matricula"}"), font=("Arial", 14), bg="#002CA7", fg="#e2e2e2")
        self.matricula.grid(row=3, column=1, padx=50)
        



        #Labels e Botões para Marcar Frequência
        
        self.entrada_horario = tk.Button(up_frame_config,text="⚙️", width=2, font=("Arial", 14), fg="#e2e2e2", bg="#002CA7")
        self.entrada_horario.grid(row=0, column=0, padx=20, pady=5)

        self.entrada_horario = tk.Label(frame_principal,text="Horário", font=("Arial", 14), width=20)
        self.entrada_horario.grid(row=0, column=1, padx=50, pady=5)
                
        self.entrada_frequencia = tk.Button(frame_principal,text="Marcar Frequência", font=("Arial", 14),background="#002CA7",fg="white", width=20)
        self.entrada_frequencia.grid(row=3, column=1, padx=50, pady=5)
        self.entrada_frequencia.focus()
        
        self.entrada_horario = tk.Entry(frame_principal, background="white", width=40) 
        self.entrada_horario.grid(row=1, column=1, padx=50, pady=5)
        

       
        

        

       



janela= tk.Tk()
app = Point(janela)
janela.mainloop()


    