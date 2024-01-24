import random
import string

def gerar_senha(comprimento, incluir_numeros, incluir_maiusculas, incluir_especiais):
    caracteres = string.ascii_letters
    if incluir_numeros:
        caracteres += string.digits
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_especiais:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

# Exemplo de uso
comprimento = int(input("Digite o comprimento da senha: "))
numeros = input("Incluir números? (s/n): ").lower() == 's'
maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
especiais = input("Incluir caracteres especiais? (s/n): ").lower() == 's'

senha_gerada = gerar_senha(comprimento, numeros, maiusculas, especiais)
print("Senha gerada:", senha_gerada)
