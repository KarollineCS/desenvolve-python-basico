# -------- Criação de variáveis
n = int(input("Insira o valor de n: "))
soma = 0
cont = 0

# -------- Estrutura de repetição
while(cont<n):
    x = int(input())
    soma += x
    cont += 1

# -------- Saída de dados
print(soma/n)