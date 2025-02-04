# ------ Biblioteca importada
from datetime import *

# ------ Tratamento de dados
hoje = datetime.now()
data_atual = hoje.strftime('%d/%m/%Y')
hora_atual = hoje.strftime('%H:%M')

# ------ Saída de dados
print(f"Data: {data_atual}")
print(f"Hora: {hora_atual}")