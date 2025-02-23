# -------- Import de bibliotecas necessárias
from random import *

# -------- Criação da lista com dados aleatórios
num_elementos = int(randrange(5, 20))
elementos = []
for i in range(num_elementos):
    elementos.append(int(randrange(1, 10)))

# -------- Lista elementos
print(f"Lista elementos:{elementos}")

# -------- Soma dos valores da lista
print(f"Soma dos valores:{sum(elementos)}")

# -------- Média de valores da lista
qtd = len(elementos)
print(f"Média de valores: {(sum(elementos)/qtd):.2f}")