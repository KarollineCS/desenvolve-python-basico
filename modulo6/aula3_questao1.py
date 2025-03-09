# ------ Definição de Variáveis
x = []

# ------ Entrada de dados
n = int(input("Digite o tamanho da lista:"))
while (n < 4):
    n = int(input("Digite o tamanho da lista:"))

# ------ Armazenamento da lista
print(f"Digite os {n} valores da lista:")
for i in range(n):
    x.append(int(input("")))

# ------ Saída de dados
print(f"Lista original:\n{x}")
print(f"Os três primeiros elementos:\n{x[0:3]}")
print(f"Os 2 últimos elementos:\n{x[n:n-3:-1]}")
print(f"Os elementos de índice par:\n{x[0::2]}")
print(f"Os elementos de índice ímpar:\n{x[1::2]}")