import pandas as pd

def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")

    novo_contato = pd.DataFrame({
        'Nome': [nome],
        'Telefone': [telefone],
        'Email': [email]
    })

    try:
        agenda = pd.read_csv('contatos.csv')
        agenda = pd.concat([agenda, novo_contato], ignore_index=True)
    except FileNotFoundError:
        agenda = novo_contato

    agenda.to_csv('contatos.csv', index=False)
    print(f"\nContato {nome} adicionado com sucesso!\n")



def listar_contatos():
    try:
        agenda = pd.read_csv('contatos.csv')
        if not agenda.empty:
            print("\nLista de Contatos:")
            print(agenda)
        else:
            print("\nA agenda de contatos está vazia.")
    except FileNotFoundError:
        print("\nA agenda de contatos está vazia.")



def buscar_contato():
    nome_busca = input("Digite o nome do contato que deseja buscar: ")
    try:
        agenda = pd.read_csv('contatos.csv')
        contato = agenda[agenda['Nome'].str.contains(nome_busca, case=False)]
        if not contato.empty:
            print("\nContato Encontrado:")
            print(contato)
        else:
            print("\nContato não encontrado.")
    except FileNotFoundError:
        print("\nA agenda de contatos está vazia.")


def remover_contato():
    nome_remover = input("Digite o nome do contato que deseja remover: ")
    try:
        agenda = pd.read_csv('contatos.csv')
        agenda = agenda[~agenda['Nome'].str.contains(nome_remover, case=False)]
        agenda.to_csv('contatos.csv', index=False)
        print(f"\nContato {nome_remover} removido com sucesso!\n")
    except FileNotFoundError:
        print("\nA agenda de contatos está vazia.")



while True:
    print("\n** Agenda de Contatos **")
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Buscar Contato")
    print("4. Remover Contato")
    print("0. Sair")

    escolha = input("\nEscolha uma opção (0-4): ")

    if escolha == '1':
        adicionar_contato()
    elif escolha == '2':
        listar_contatos()
    elif escolha == '3':
        buscar_contato()
    elif escolha == '4':
        remover_contato()
    elif escolha == '0':
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")