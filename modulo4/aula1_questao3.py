# ------ Entrada de dados
n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Insira a segunda nota: "))
n3 = float(input("Insira a terceira nota: "))

# ------ Tratamento de dados
m = (n1 + n2 + n3)/3

# ------ Condicional
if(m>=60):
    print("Aprovado")
elif(m>=40 and m<60):
    print("Recuperação")
else:
    print("Reprovado")

# ------ Saída
print("Fim")