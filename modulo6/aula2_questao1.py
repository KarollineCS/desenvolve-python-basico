# -------- Import de bibliotecas necessárias
from random import *

# -------- Criação da lista com dados aleatórios
lista = []
for i in range(0,19,1):
    lista.append(int(randrange(-100, 100)))

# -------- Lista ordenada, sem modificar a lista original
print(f"Lista ordenada:\n{sorted(lista)}")

# -------- Lista original
print(f"Lista original:\n{lista}")

# -------- Índice do maior valor da lista
print(f"Maior valor: {max(lista)}")

# -------- Índice do menor valor da lista
print(f"Menor valor: {min(lista)}")
