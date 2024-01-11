# Dia 01: Identificador de Números Pares e Ímpares.
# entrada de dados => input()
#estrutura de controle => if/else

def identificar_numero(numero):
    if numero %2 == 0:
        return "Par"
    else:
        return "Ímpar"
    
numero = int(input("Digite um numero: "))
resultado = identificar_numero(numero) 
print(f"o número {numero} é {resultado}")   