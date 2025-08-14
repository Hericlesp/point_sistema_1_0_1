import tkinter as tk
from tkinter import ttk 

class Inicial:
    def __init__(self, root):
        self.root = root
        self.root.title("Aparencer")
        self.root.geometry("1080x720")

        # Create a style object
        self.style = ttk.Style()

        # Configure the style for the main window
        self.style.configure("TFrame", background="lightblue")
        self.style.configure("TButton", background="lightgreen", foreground="black")

        # Create a frame with the configured style
        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.configure(style="TFrame")
        # Configure the grid layout
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Add a label to the frame
        self.label = ttk.Label(self.frame, text="nome da pessoal admitrativa do banco de dados  ", font=("Arial", 16))
        self.label.grid(row=0, column=1, pady=20, padx=20, sticky="nsew") 
        
        # Add a label to the frame
        self.label = ttk.Label(self.frame, text="Nome do professor", font=("Arial", 16))
        self.label.grid(row=1, column=0, pady=20, padx=20, sticky="nsew")
        
        # Add a text entry field to the frame
        self.entry = ttk.Entry(self.frame, width=30)
        self.entry.grid(row=1, column=1, pady=10, padx=20, sticky="nsew")   
         
        # Add a label to the frame
        self.label = ttk.Label(self.frame, text="CPF", font=("Arial", 16))
        self.label.grid(row=2, column=0, pady=20, padx=20, sticky="nsew") 
        
        # Add a text entry field to the frame
        self.entry = ttk.Entry(self.frame, width=30)
        self.entry.grid(row=2, column=1, pady=10, padx=20, sticky="nsew")    
         
        # Add a label to the frame
        self.label = ttk.Label(self.frame, text="Telefone", font=("Arial", 16))
        self.label.grid(row=3, column=0, pady=20, padx=20, sticky="nsew") 
        
        # Add a text entry field to the frame
        self.entry = ttk.Entry(self.frame, width=30)
        self.entry.grid(row=3, column=1, pady=10, padx=20, sticky="nsew")   
         
        # Add a label to the frame
        self.label = ttk.Label(self.frame, text="E-mail", font=("Arial", 16))
        self.label.grid(row=4, column=0, pady=20, padx=20, sticky="nsew")
        
        # Add a text entry field to the frame
        self.entry = ttk.Entry(self.frame, width=30)
        self.entry.grid(row=4, column=1, pady=10, padx=20, sticky="nsew")   
         
        # Add a label to the frame
        self.label = ttk.Label(self.frame, text="Matricula", font=("Arial", 16))
        self.label.grid(row=5, column=0, pady=20, padx=20, sticky="nsew")
        
        # Add a text entry field to the frame
        self.entry = ttk.Entry(self.frame, width=30)
        self.entry.grid(row=5, column=1, pady=10, padx=20, sticky="nsew")  
        
        # Add a label to the frame
        self.label = ttk.Label(self.frame, text="Curso 1", font=("Arial", 16))
        self.label.grid(row=6, column=0, pady=20, padx=20, sticky="nsew")
        
        # Add a text entry field to the frame
        self.entry = ttk.Entry(self.frame, width=30)
        self.entry.grid(row=6, column=1, pady=10, padx=20, sticky="nsew")
        
        # Add a label to the frame
        self.label = ttk.Label(self.frame, text="Curso 2", font=("Arial", 16))
        self.label.grid(row=7, column=0, pady=20, padx=20, sticky="nsew") 
        
        # Add a text entry field to the frame
        self.entry = ttk.Entry(self.frame, width=30)
        self.entry.grid(row=7, column=1, pady=10, padx=20, sticky="nsew")
        # Add a label to the frame
        self.label = ttk.Label(self.frame, text="Curso 3", font=("Arial", 16))
        self.label.grid(row=8, column=0, pady=20, padx=20, sticky="nsew") 
        
        # Add a text entry field to the frame
        self.entry = ttk.Entry(self.frame, width=30)
        self.entry.grid(row=8, column=1, pady=10, padx=20, sticky="nsew")
        # Add a label to the frame
        self.label = ttk.Label(self.frame, text="Curso 4", font=("Arial", 16))
        self.label.grid(row=9, column=0, pady=20, padx=20, sticky="nsew") 
        
        # Add a text entry field to the frame
        self.entry = ttk.Entry(self.frame, width=30)
        self.entry.grid(row=9, column=1, pady=10, padx=20, sticky="nsew")
        # Add a button to the frame
        self.button = ttk.Button(self.frame, text="Cadastrar", command=lambda: print("Cadastrado!"))
        self.button.grid(row=10, column=1, pady=20, padx=20, sticky="nsew")
        
           
    def run(self):
        self.root.mainloop()
        
        
        
        
        
        
        
        
if __name__ =="__main__":
             
    root = tk.Tk()
    app = Inicial(root)
    root.mainloop()
