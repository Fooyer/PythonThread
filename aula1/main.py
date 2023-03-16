import threading
import tkinter as tk
from tabela import Tabela
from supabasetest import getProfiles
from formulario import Formulario

def monta_tabela():

    headers = ["UID","Username","Email"]
    dados = getProfiles()

    root = tk.Tk()
    root.title('Tabela gerada com Thread 1')
    tabela = Tabela(root, 15, 3, headers, dados.data)
    root.mainloop()

def monta_formulario():
    root2 = tk.Tk()
    root2.geometry('400x300')
    root2.title('Formulário gerado com Theead 2')

    formulario = Formulario(root2)

    root2.mainloop()

    print("Cadastro gerado com Thread 2")

t1 = threading.Thread(target=monta_tabela)
t2 = threading.Thread(target=monta_formulario)
t1.start()
t2.start()

print("Fim da Thread Principal")