# ------ Biblioteca importada
from math import *
from decimal import *

# ------ Entrada de dados
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

# ------ Tratamento de dados
dif = abs(n1-n2)

# ------ Saída de dados
print(f"A diferença absoluta entre os números é: {round(dif, 2)}")
