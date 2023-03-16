import tkinter as tk

class Formulario:
    def __init__(self, master):
        self.master = master
        
        # Labels
        tk.Label(master, text='Nome:').grid(row=0, column=0, padx=5, pady=5)
        tk.Label(master, text='Idade:').grid(row=1, column=0, padx=5, pady=5)
        tk.Label(master, text='Sexo:').grid(row=2, column=0, padx=5, pady=5)

        # Entradas de texto
        self.nome_entry = tk.Entry(master)
        self.nome_entry.grid(row=0, column=1, padx=5, pady=5)

        self.idade_entry = tk.Entry(master)
        self.idade_entry.grid(row=1, column=1, padx=5, pady=5)

        # Radio buttons para o sexo
        self.sexo_var = tk.StringVar()
        tk.Radiobutton(master, text='Masculino', variable=self.sexo_var, value='Masculino').grid(row=2, column=1, padx=5, pady=5)
        tk.Radiobutton(master, text='Feminino', variable=self.sexo_var, value='Feminino').grid(row=3, column=1, padx=5, pady=5)

        # Botão submit
        submit_button = tk.Button(master, text='Enviar', command=self.submit)
        submit_button.grid(row=4, column=1, padx=5, pady=5)
        
    def submit(self):
        nome = self.nome_entry.get()
        idade = self.idade_entry.get()
        sexo = self.sexo_var.get()
        print(f'Nome: {nome}\nIdade: {idade}\nSexo: {sexo}')
