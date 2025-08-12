import tkinter as tk
from tkinter import ttk,messagebox
from datetime import datetime
import random

class POINT:
    def __init__(self,janela):
        self.janela = janela 
        self.janela.title("ÁREA DO DOCENTE") 
        self.janela.geometry("800x600")

        
 
        self.style = ttk.Style()  
        self.style.theme_use("clam")
        self.lancar_chamada() 

    def lancar_chamada(self):
        frame_principal = ttk.Frame(self.janela,padding=30)
        frame_principal.pack(fill=tk.BOTH,expand=True)

        Entrada_frame = ttk.Frame(frame_principal,padding=4)
        Entrada_frame.pack(fill=tk.X)

        ttk.Label(Entrada_frame,text="CÓDIGO DE CHAMADA:").grid(row=0,column=3) 
        self.Entrada_tarefa = ttk.Entry(Entrada_frame,width=20) 
        self.Entrada_tarefa.grid(row=1,column=3,pady=5)
        self.Entrada_tarefa.focus()
        


        def gerar_codigo():
            codigo = f"{random.randint(10, 99)}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.choice('abcdefghijklmnopqrstuvwxyz')}{random.randint(10, 99)}" 
            self.Entrada_tarefa.delete(0, tk.END)   
            self.Entrada_tarefa.insert(0, codigo)                                                       #LETRA MINÚSCULA PODE CAUSAR CONFUSÃO 




        ttk.Button(Entrada_frame, text="GERAR CÓDIGO", command=gerar_codigo,).grid(row=2, column=3)
        


        ttk.Label(Entrada_frame,text="Situação do aluno").grid(row=3,column=3) 
        self.prioridade = tk.StringVar(value="")
        ttk.Combobox(Entrada_frame,textvariable=self.prioridade,values=["Ausente", "Presente"],state="readonly").grid(row=4,column=3,padx=5)   #escrever dentro de uma caixa de seleção e abrir a lista apenas para leitura
        ttk.Label(Entrada_frame,text="Data").grid(row=5,column=3)
    
        self.entrada_data = ttk.Entry(Entrada_frame,width=20)
        self.entrada_data.grid(row=6,column=3)
        self.entrada_data.insert(0,datetime.now().strftime("%d/%m/%Y")) 


        # APRESENTAR TODOS OS ALUNOS E QUAL A SITUAÇÃO DOS MESMOS(AUSENTE OU PRESENTE)
        
        self.tree = ttk.Treeview(frame_principal,columns=("Data","R.A.","Aluno", "Situação","Curso"),show="headings",selectmode="browse")


        self.tree.column("Data",width=100, anchor=tk.CENTER)
        self.tree.heading("Data",text="Data")
        
        self.tree.column("R.A.",width=30, anchor=tk.CENTER)
        self.tree.heading("R.A.",text="R.A.")

        self.tree.column("Aluno",width=150, anchor=tk.CENTER)
        self.tree.heading("Aluno",text="Aluno") 

        self.tree.column("Situação",width=200, anchor=tk.CENTER)
        self.tree.heading("Situação",text="Situação") 

        self.tree.column("Curso",width=80, anchor=tk.CENTER)
        self.tree.heading("Curso",text="Curso") 

        
        self.tree.pack(fill=tk.BOTH, expand=True,pady=10)

# FUNÇÃO: MARCAR PRESENÇA MANUALMENTE CASO O ALUNO NÃO TENHA ACESSO E ALGUM MODO AO SISTEMA. 

if __name__=="__main__":
    janela= tk.Tk()
    app=POINT(janela)
    janela.mainloop()





















































































































