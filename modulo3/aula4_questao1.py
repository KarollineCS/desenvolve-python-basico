# -------- Entrada de dados
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

# -------- Soma e verificação do valor
soma = n1+n2
if (soma%2 == 0):
    print(f"a soma dos valores é par: {soma}")
else:
    print(f"a soma dos valores é ímpar: {soma}")
