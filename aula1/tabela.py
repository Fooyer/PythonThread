import tkinter as tk


class Tabela:
    def __init__(self, janela, linhas, colunas, headers=None, dados=None):
        self.linhas = linhas
        self.colunas = colunas
        self.headers = headers
        self.dados = dados
        self.criar_tabela(janela)

    def criar_tabela(self, janela):
        janela.configure(bg='black')
        
        # Define o tamanho e uniformidade das colunas
        for i in range(self.colunas):
            janela.grid_columnconfigure(i, minsize=500, uniform='col')

        # Cria os frames e labels da tabela
        for i in range(self.linhas + 1):  # Adiciona uma linha extra para o cabeçalho

            for j in range(self.colunas):

                # Se for um header cria com cor aqua, caso contrário white

                if i == 0 and self.headers:
                    frame = tk.Frame(master=janela, bg='aqua', bd=1, relief="flat")
                else:
                    frame = tk.Frame(master=janela, bg='white', bd=1, relief="flat")

                # Cria o frame no grid

                frame.grid(row=i, column=j, padx=1, pady=1, sticky="nsew")

                if i == 0 and self.headers:  # Se for a primeira linha e houver um cabeçalho definido
                    label = tk.Label(master=frame, text=self.headers[j], bg='aqua', highlightbackground='aqua') 
                else:
                    label = tk.Label(master=frame, text=f'{self.dados[j]["id"]}', bg='white', highlightbackground='white')
                
                label.pack(pady=5, padx=5)
                frame.columnconfigure(0, weight=1)
                frame.rowconfigure(0, weight=1)