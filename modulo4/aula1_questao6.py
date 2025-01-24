# --------- Entrada de dados
n = int(input("Qtd de experimentos registrados: "))
cont = 0
total = 0
soma_c = 0
soma_r = 0
soma_s = 0

# --------- Tratamento de dados
while(cont<n):
    # --- Pega entrada no formato informado
    entrada = input()
    # --- divide a entrada em substrings separadas por espaço
    # q eh quantia e t eh tipo
    q, t = entrada.split()
    # --- garante que q seja um inteiro
    q = int(q)
    if(t == 'C' or t == 'c'):
        soma_c += q
    elif(t == 'R' or t == 'r'):
        soma_r += q
    elif(t == 'S' or t == 's'):
        soma_s += q

    total += q
    cont += 1

# --------- Cálculo de porcentagem dos cobaias
porc_c = (soma_c*100)/total
porc_r = (soma_r*100)/total
porc_s = (soma_s*100)/total

# --------- Saída de dados
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {soma_c}")
print(f"Total de ratos: {soma_r}")
print(f"Total de sapos: {soma_s}")
print(f"Percentual de coelhos: {porc_c:.2f}%")
print(f"Percentual de ratos: {porc_r:.2f}%")
print(f"Percentual de sapos: {porc_s:.2f}%")