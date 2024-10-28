# ----------Entrada de dados
idade=int(input("Digite sua idade: "))
tab=bool(input("Já jogou pelo menos 3 jogos: "))
jogos=int(input("Digite quantos jogos já venceu: "))

# ----------Verifica as variaveis que possuem limitação
verifica_id = ((idade >= 16) or (idade <= 18))
verifica_jg = (jogos >= 1)

# ----------Verificação de cada variável separadamente
#print(verifica_id)
#print(verifica_jg)
#print(tab)

# ----------Retorna resultado ao usuário
print("Apto para ingressar no clube de jogos de tabuleiro: ", (verifica_id and verifica_jg and tab))