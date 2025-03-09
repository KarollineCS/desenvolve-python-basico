# ------ Definição de Variáveis
links = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

# ------ Tratamento da lista
dominios = [link[4:-4] for link in links]

# ------ Saída de dados
print(f"Urls: {links}")
print(f"Dominios: {dominios}")