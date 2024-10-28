# ---------- Entrada de dados
classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ")
pts_forca = int(input("Digite os pontos de força (de 1 a 20): "))
pts_magia = int(input("Digite os pontos de magia (de 1 a 20): "))

# ---------- Verificação de dados conforme requisitado
verifica = (((classe == 'guerreiro') and (pts_forca >= 15) and (pts_magia <= 10))
            or ((classe == 'mago') and (pts_forca <= 10) and (pts_magia >= 15))
            or ((classe == 'arqueiro') and (5 <= pts_forca <= 15) and (5 <= pts_magia <=15)))

# ---------- Saída tratada para o usuário
print("Pontos de atributo consistentes com a classe escolhida:",verifica)