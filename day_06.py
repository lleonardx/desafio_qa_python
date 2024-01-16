def quilometros_para_milhas(quilometros):
    return quilometros * 0.621371

def milhas_para_quilometros(milhas):
    return milhas * 1.60934

def metros_para_pes(metros):
    return metros * 3.28084

def pes_para_metros(pes):
    return pes * 0.3048

def celsius_para_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Função para receber dados do usuário e realizar as conversões
def realizar_conversoes():
    opcao = input("Escolha a conversão (1 - Km para Milhas, 2 - Milhas para Km, 3 - Metros para Pés, 4 - Pés para Metros, 5 - Celsius para Fahrenheit, 6 - Fahrenheit para Celsius): ")

    if opcao in ['1', '2', '3', '4', '5', '6']:
        valor = float(input("Digite o valor a ser convertido: "))

        if opcao == '1':
            resultado = quilometros_para_milhas(valor)
            unidade_origem = 'quilômetros'
            unidade_destino = 'milhas'
        elif opcao == '2':
            resultado = milhas_para_quilometros(valor)
            unidade_origem = 'milhas'
            unidade_destino = 'quilômetros'
        elif opcao == '3':
            resultado = metros_para_pes(valor)
            unidade_origem = 'metros'
            unidade_destino = 'pés'
        elif opcao == '4':
            resultado = pes_para_metros(valor)
            unidade_origem = 'pés'
            unidade_destino = 'metros'
        elif opcao == '5':
            resultado = celsius_para_fahrenheit(valor)
            unidade_origem = 'graus Celsius'
            unidade_destino = 'graus Fahrenheit'
        else:
            resultado = fahrenheit_para_celsius(valor)
            unidade_origem = 'graus Fahrenheit'
            unidade_destino = 'graus Celsius'

        print(f"{valor} {unidade_origem} é igual a {resultado:.2f} {unidade_destino}")
    else:
        print("Opção inválida.")

# Chamando a função para realizar as conversões
realizar_conversoes()
