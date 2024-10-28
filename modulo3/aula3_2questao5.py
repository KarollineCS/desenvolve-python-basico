# ---------- Entrada de dados
genero = input("Digite seu gênero (M ou F): ")
idade = int(input("Digite sua idade: "))
tempo_s = int(input("Digite seu tempo de serviço: "))

# ---------- Verificação de dados conforme requisitado
verifica = ((((genero == 'F') and (idade >= 60)) or ((genero == 'M') and (idade >= 65))) 
            or (tempo_s >= 30) or ((idade >= 60) and (tempo_s >= 25)))

# ---------- Saída tratada para o usuário
print("Possibilidade de se aposentar:",verifica)