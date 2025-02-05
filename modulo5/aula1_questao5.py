# ------ Biblioteca importada
from emoji import *

# ------ Entrada de dados
print("Emojis disponíveis:")
print(f"{emojize(':red_heart:', language='alias')} - :red_heart:")
print(f"{emojize(':thumbsup:', language='alias')} - :thumbsup:")
print(f"{emojize(':thinking_face:', language='alias')} - :thinking_face:")
print(f"{emojize(':partying_face:', language='alias')} - :partying_face:")

x = input("Digite uma frase e ela será emojizada:\n")

# ------ Tratamento de dados
# ------ Saída de dados
print(emojize(x, language="alias"))