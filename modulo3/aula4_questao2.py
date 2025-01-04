# --------- Entrada de dados
x = int(input("Insira a nota de avaliação do filme: "))

# --------- Condicionais de saída
if (x == 5):
    print("Excelente!")
elif (x == 4):
    print("Muito bom!")
elif (x == 3):
    print("Bom!")
elif (x == 2):
    print("Regular.")
elif (x == 1):
    print("Ruim.")
else:
    print("Nota fora do escopo de avaliação")