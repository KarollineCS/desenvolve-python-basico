valor = int(input("Valor:"))

# Processamento
#### Começar da maior nota
n_100 = int(valor//100) # 576//100 = 5
#### Atualizar quanto falta depois da maior nota
valor = valor % 100 # 576-(5*100) = 76

n_50 = int(valor//50) # 76//50 = 1
valor = valor % 50 # 26

n_20 = int(valor//20) # 26//20 = 1
valor = valor % 20 # 6

n_10 = int(valor//10) # 6//10 = 0
valor = valor % 10 # 6

n_5 = int(valor//5) # 6//5 = 1
valor = valor % 5 # 1

n_2 = int(valor//2) # 1//2 = 0
valor = valor % 2 # 1

n_1 = valor

# Impressão de dados
print(f"{n_100} nota(s) de R$100\n")
print(f"{n_50} nota(s) de R$50\n")
print(f"{n_20} nota(s) de R$20\n")
print(f"{n_10} nota(s) de R$10\n")
print(f"{n_5} nota(s) de R$5\n")
print(f"{n_2} nota(s) de R$2\n")
print(f"{n_1} nota(s) de R$1\n")
