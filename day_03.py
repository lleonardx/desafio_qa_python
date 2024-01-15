def verificar_palindromo(texto):
    texto = texto.replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "").lower()
    
    return texto == texto[::-1]

texto_usuario = input("Digite uma palavra ou frase: ")

print("É um palindromo." if verificar_palindromo(texto_usuario) else "Não é um palindromo")