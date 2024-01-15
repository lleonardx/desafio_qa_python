#Função para dividir o texto em palavras
def contar_palavras(texto):
    palavras = texto.split()
    numero_palavras = len(palavras)
    
    #Contando o numero de palavras
    return numero_palavras

texto_usuario = input("Digite um texto: ")

resultado = contar_palavras(texto_usuario)
print(f"O numero de palavras no texto é: {resultado}")
