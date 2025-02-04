# ------ Biblioteca importada
from random import *

# ------ Entrada de dados
x = int(randrange(1, 10))

# ------ Tratamento de dados
while True:
    n = int(input("Adivinhe o número entre 1 e 10: "))
    if (n > 0 and n < 11):
        if (n > x):
            print("Muito alto, tente novamente!")
        elif (n < x):
            print("Muito baixo, tente novamente!")
        else: break
    else:
        print("Entrada inválida")

# ------ Saída de dados
print(f"Correto! O número é {x}")