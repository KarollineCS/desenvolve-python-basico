# -------- Função para intercalar as listas
def intercalar_listas(lista1, lista2):
    intercalada = []
    tamanho_min = min(len(lista1), len(lista2))
    
    # Intercalando os elementos
    for i in range(tamanho_min):
        intercalada.append(lista1[i])
        intercalada.append(lista2[i])
    
    # Adicionando os elementos restantes
    intercalada.extend(lista1[tamanho_min:])
    intercalada.extend(lista2[tamanho_min:])
    
    return intercalada

# -------- Criação da lista 1
lista1 = []
n = int(input("Digite a quantidade de elementos da lista 1: "))
print(f"Digite os {n} números da lista 1: ")
for i in range(n):
    lista1.append(int(input()))

# -------- Criação da lista 2
lista2 = []
m = int(input("Digite a quantidade de elementos da lista 2: "))
print(f"Digite os {m} números da lista 2: ")
for i in range(m):
    lista2.append(int(input()))

# -------- Criando a lista intercalada
lista_intercalada = intercalar_listas(lista1, lista2)
print("Lista Intercalada:", lista_intercalada)