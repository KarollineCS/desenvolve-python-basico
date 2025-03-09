# -------- Import de bibliotecas necessárias
from random import *

# -------- Criação da lista com dados aleatórios
lista = []
for i in range(0,19,1):
    lista.append(int(randrange(-10, 10)))

# -------- Saída e tratamento de dados
print(f"Original: {lista}")

max_negativos = 0
indice_inicio = 0

for i in range(len(lista) - 2):
    sublista = lista[i:i+3]
    negativos = sum(1 for num in sublista if num < 0)
    
    if negativos > max_negativos:
        max_negativos = negativos
        indice_inicio = i

del lista[indice_inicio:indice_inicio+3]

print(f"Editada: {lista}")