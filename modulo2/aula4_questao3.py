# Define o nome do produto nas chamadas de variável p* (onde * é o indíce do produto)
p1 = input("Digite o nome do produto 1: ")
# Define o preço unitário do produto nas chamadas de variável v*
v1 = float(input("Digite o preço unitário do produto 1: "))
# Define a quantidade do produto nas chamadsa de variável q*
q1 = int(input("Digite a quantidade do produto 1:"))

p2 = input("Digite o nome do produto 2: ")
v2 = float(input("Digite o preço unitário do produto 2: "))
q2 = int(input("Digite a quantidade do produto 2:"))

p3 = input("Digite o nome do produto 3: ")
v3 = float(input("Digite o preço unitário do produto 3: "))
q3 = int(input("Digite a quantidade do produto 3:"))

# Retorna ao usuário o valor total, já realizando a multiplicação dos produtos pelas suas quantidades e a soma dos mesmos
print(f"Total: R${(v1*q1)+(v2*q2)+(v3*q3):,.2f}")

