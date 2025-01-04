# --------- Entrada de dados
km = int(input("Insira a distancia em km: "))
kg = float(input("Insira o peso do pacote em kg: "))

# --------- Tratamento de dados
if (km <= 100):
    entrega = kg*1
    if (kg > 10):
        entrega = entrega + 10
    print(f"O valor da entrega eh: R${entrega}")
elif ((km > 100) and (km <= 300)):
    entrega = kg*1.5
    if (kg > 10):
        entrega = entrega + 10
    print(f"O valor da entrega eh: R${entrega}")
else:
    entrega = kg*2
    if (kg > 10):
        entrega = entrega + 10
    print(f"O valor da entrega eh: R${entrega}")