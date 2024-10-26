#pede ao usuário os valores de cada variável do tipo float
largura=float(input("Qual a largura do terreno?\n"))
comprimento=float(input("Qual o comprimento?\n"))
preco_m2=float(input("Digite o preço do m²: "))

#realiza o cálculo da área por m2 e o preço total dessa área
area_m2 = comprimento * largura
preco_total = preco_m2 * area_m2

#retorna ao usuário o tamanho da área total e o preço total
print(f"O terreno possui {area_m2}m² e custa R${preco_total:,.2f}")
