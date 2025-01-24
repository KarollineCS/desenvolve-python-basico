# -------- Criação de variáveis
n = int(input("Insira o valor de n: "))
maior = 0

# -------- Estrutura de repetição
while(n>0):
    x = int(input())
    while(x>maior):
        maior = x
    n -= 1

# -------- Saída de dados
print(maior)