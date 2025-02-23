# -------- Import de bibliotecas necessárias
from random import *

# -------- Criação da lista com dados aleatórios
lista1 = []
lista2 = []
for i in range(0, 10, 1):
    lista1.append(int(randrange(0, 50)))
    lista2.append(int(randrange(0, 50)))
# -------- Tratamento de interseção
intersecao = sorted([num for num in set(lista1) if num in lista2])

# -------- Listas
print(f"Lista1 - {lista1}")
print(f"Lista2 - {lista2}")
print(f"Intersecção - {intersecao}")

# -------- Contagem de itens
print("Contagem")
for i in range(len(intersecao)):
    print(f"{intersecao[i]}: (lista1={lista1.count(intersecao[i])}, lista2={lista2.count(intersecao[i])})")