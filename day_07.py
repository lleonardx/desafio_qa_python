import time

def temporizador(segundos):
    while segundos > 0:
        print(f"Tempo restante: {segundos} segundos")
        time.sleep(1)  # Aguarda 1 segundo
        segundos -= 1

    print("Tempo encerrado!")

def contador_regressivo(segundos):
    for i in range(segundos, 0, -1):
        print(f"Tempo restante: {i} segundos")
        time.sleep(1)  # Aguarda 1 segundo

    print("Contagem regressiva encerrada!")

# Solicitação de escolha ao usuário
opcao = input("Escolha a opção (1 - Temporizador, 2 - Contador Regressivo): ")

if opcao == '1':
    tempo_desejado = int(input("Digite o tempo desejado em segundos: "))
    temporizador(tempo_desejado)
elif opcao == '2':
    tempo_desejado = int(input("Digite o tempo desejado em segundos: "))
    contador_regressivo(tempo_desejado)
else:
    print("Opção inválida.")
