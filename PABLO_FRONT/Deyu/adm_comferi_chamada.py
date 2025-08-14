import tkinter as tk
from tkinter import ttk

class ConsultaChamada:
    def __init__(self, root):
        self.root = root
        self.root.title("Consulta de Chamada por Turma")
        self.root.geometry("900x600")
        self.root.configure(bg="#f0f8ff")

        # Estilo
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f8ff")
        self.style.configure("TLabel", background="#f0f8ff", font=("Arial", 12))
        self.style.configure("TButton", font=("Arial", 10, "bold"))
        self.style.configure("Treeview.Heading", font=("Arial", 10, "bold"))

        # Frame principal
        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.pack(fill="both", expand=True)

        # Título
        self.label_titulo = ttk.Label(self.frame, text="Consulta de Chamada", font=("Arial", 18, "bold"))
        self.label_titulo.pack(pady=10)

        # Combobox de turmas
        self.label_turma = ttk.Label(self.frame, text="Selecione a Turma:")
        self.label_turma.pack(pady=5)

        self.combo_turmas = ttk.Combobox(self.frame, values=["Turma 1", "Turma 2", "Turma 3"])
        self.combo_turmas.pack(pady=5)

        # Botão buscar
        self.btn_buscar = ttk.Button(self.frame, text="Buscar Chamada")
        self.btn_buscar.pack(pady=10)

        # Tabela de chamada
        self.tree = ttk.Treeview(self.frame, columns=("matricula", "nome", "presenca"), show="headings", height=15)
        self.tree.heading("matricula", text="Matrícula")
        self.tree.heading("nome", text="Nome")
        self.tree.heading("presenca", text="Presença")
        self.tree.column("matricula", width=150)
        self.tree.column("nome", width=400)
        self.tree.column("presenca", width=100)
        self.tree.pack(pady=20)

        # Mensagem (caso necessário)
        self.label_mensagem = ttk.Label(self.frame, text="")
        self.label_mensagem.pack()

# Execução
if __name__ == "__main__":
    root = tk.Tk()
    app = ConsultaChamada(root)
    root.mainloop()
