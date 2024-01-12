def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
        # Usamos // para garantir a divisão inteira
        return x // y
    else:
        return "Erro: Divisão por zero!"

# Função principal
def calculadora():
    while True:
        print("Escolha a operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Digite o número da operação desejada: ")

        if escolha == '5':
            print("Encerrando a calculadora.")
            break

        if escolha in ('1', '2', '3', '4'):
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))

            if escolha == '1':
                print(f"{num1} + {num2} = {soma(num1, num2)}")
            elif escolha == '2':
                print(f"{num1} - {num2} = {subtracao(num1, num2)}")
            elif escolha == '3':
                print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")
            elif escolha == '4':
                resultado_divisao = divisao(num1, num2)
                if isinstance(resultado_divisao, int):
                    print(f"{num1} / {num2} = {resultado_divisao}")
                else:
                    print(resultado_divisao)
        else:
            print("Opção inválida. Por favor, escolha uma operação válida.")

# Chamando a função principal
calculadora()
