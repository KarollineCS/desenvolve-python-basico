# ------ Biblioteca importada
from math import *
from random import *
from decimal import *

# ------ Entrada de dados
n = int(input("Informe uma quantidade de valores inteiros: "))
soma = 0

# ------ Tratamento de dados
for i in range(n):
    x = int(randrange(1, 100))
    print(f"Valor {i}: {x}")
    soma += x
    

# ------ Saída de dados
print(f"Soma total: {soma}")
total = sqrt(soma)
print(f"A raíz quadrada da soma dos números é: {round(total, 4)}")