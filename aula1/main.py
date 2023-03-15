import threading
import tkinter as tk
from tabela import Tabela
from supabasetest import getProfiles
import json

def monta_tabela():

    headers = ["UID","Username","Email"]
    dados = getProfiles()

    print(dados.data[1])

    root = tk.Tk()
    root.title('Tabela gerada com Thread 1')
    tabela = Tabela(root, 2, 3, headers, dados.data)
    root.mainloop()

def monta_formulario():
    print("Cadastro gerado com Thread 2")

t1 = threading.Thread(target=monta_tabela)
t2 = threading.Thread(target=monta_formulario)
t1.start()
t2.start()

print("Fim")