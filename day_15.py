import csv

def criar_arquivo_csv():
    with open('biblioteca.csv', 'w', newline='', encoding='utf-8') as arquivo:
        colunas = ['Título', 'Autor', 'Ano de Publicação']
        escritor_csv = csv.DictWriter(arquivo, fieldnames=colunas)
        escritor_csv.writeheader()

def adicionar_livro(titulo, autor, ano):
    with open('biblioteca.csv', 'a', newline='', encoding='utf-8') as arquivo:
        colunas = ['Título', 'Autor', 'Ano de Publicação']
        escritor_csv = csv.DictWriter(arquivo, fieldnames=colunas)

        escritor_csv.writerow({'Título': titulo, 'Autor': autor, 'Ano de Publicação': ano})

def listar_livros():
    with open('biblioteca.csv', 'r', newline='', encoding='utf-8') as arquivo:
        leitor_csv = csv.DictReader(arquivo)
        for row in leitor_csv:
            print(f"Título: {row['Título']}, Autor: {row['Autor']}, Ano: {row['Ano de Publicação']}")

# Criar o arquivo CSV se não existir
criar_arquivo_csv()

# Menu interativo
while True:
    print("\n=== Gerenciador de Biblioteca Pessoal ===")
    print("1. Adicionar Livro")
    print("2. Listar Livros")
    print("3. Sair")

    escolha = input("Escolha uma opção (1/2/3): ")

    if escolha == '1':
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o nome do autor: ")
        ano = input("Digite o ano de publicação: ")
        adicionar_livro(titulo, autor, ano)

    elif escolha == '2':
        print("\n=== Lista de Livros ===")
        listar_livros()

    elif escolha == '3':
        print("Saindo do programa. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
