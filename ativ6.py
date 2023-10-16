import datetime

def informações_do_usuário(ussnm, pssd):
    nome = input("Digite seu nome: ")
    endereço = input("Seu endereço: ")
    idade = input("Sua idade: ")
    ussnm_ = ussnm + " tarefas.txt"
    f = open(ussnm_, 'a')
    f.write(pssd)
    f.write("\nNome: ")
    f.write(nome)
    f.write('\n')
    f.write("Endereço: ")
    f.write(endereço)
    f.write('\n')
    f.write("Idade: ")
    f.write(idade)
    f.write('\n')
    f.close()

def inscrever():
    print("Digite o nome de usuário com o qual deseja acessar sua conta")
    nome_de_usuário = input("Por favor, insira aqui: ")
    senha = input("Digite a senha: ")
    informações_do_usuário(nome_de_usuário, senha)
    print("Prossiga para o login")
    login()

def login():
    print("Digite seu nome de usuário")
    nome_de_usuário = input("Insira aqui: ")

    senha_digitada = (input("Digite a senha")) + '\n'
    try:
        nome_de_usuário_arquivo = nome_de_usuário + " tarefas.txt"
        f_ = open(nome_de_usuário_arquivo, 'r')

        k = f_.readlines(0)[0]
        f_.close()

        if senha_digitada == k:
            print(
                "1 - para visualizar seus dados\n2 - Para adicionar tarefa\n3 - Atualizar tarefa\n4 - VISUALIZAR STATUS DA TAREFA")
            a = input()

            if a == '1':
                visualizar_dados(nome_de_usuário_arquivo)
            elif a == '2':
                informações_da_tarefa(nome_de_usuário_arquivo)
            elif a == '3':
                atualizar_tarefa(nome_de_usuário)
            elif a == '4':
                visualizar_status_da_tarefa(nome_de_usuário)
            else:
                print("Entrada incorreta! Por favor, insira a entrada correta.")
        else:
            print("SUA SENHA OU NOME DE USUÁRIO ESTÁ ERRADO")
            login()

    except Exception as e:
        print(e)
        login()

def visualizar_dados(nome_de_usuário):
    ff = open(nome_de_usuário, 'r')
    print(ff.read())
    ff.close()

def informações_da_tarefa(nome_de_usuário):
    print("Digite o número de tarefas que deseja ADICIONAR")
    j = int(input())
    f1 = open(nome_de_usuário, 'a')

    for i in range(1, j + 1):
        tarefa = input("Digite a tarefa: ")
        objetivo = input("Digite o objetivo: ")
        pp = "TAREFA " + str(i) + ' :'
        qq = "OBJETIVO " + str(i) + " :"

        f1.write(pp)
        f1.write(tarefa)
        f1.write('\n')
        f1.write(qq)
        f1.write(objetivo)
        f1.write('\n')
        print("Deseja parar? Pressione a barra de espaço, caso contrário, pressione Enter")
        s = input()
        if s == ' ':
            break
    f1.close()

def atualizar_tarefa(nome_de_usuário):
    nome_de_usuário = nome_de_usuário + " TAREFA.txt"
    print("Por favor, insira as tarefas que foram concluídas: ")
    tarefa_concluída = input()

    print("Insira as tarefas que ainda não foram iniciadas por você: ")
    tarefa_não_iniciada = input()

    print("Insira as tarefas que você está realizando: ")
    tarefa_em_andamento = input()

    fw = open(nome_de_usuário, 'a')
    DT = str(datetime.datetime.now())
    fw.write(DT)
    fw.write("\n")
    fw.write("TAREFA CONCLUÍDA\n")
    fw.write(tarefa_concluída)
    fw.write("\n")
    fw.write("TAREFA EM ANDAMENTO\n")
    fw.write(tarefa_em_andamento)
    fw.write("\n")
    fw.write("NÃO INICIADO AINDA\n")
    fw.write(tarefa_não_iniciada)
    fw.write("\n")

def visualizar_status_da_tarefa(nome_de_usuário):
    nome_de_usuário = nome_de_usuário + " TAREFA.txt"
    o = open(nome_de_usuário, 'r')
    print(o.read())
    o.close()

if __name__ == '__main__':
    print("BEM-VINDO AO GERENCIADOR DE TAREFAS DO ANURAG")
    print("Você é novo neste software?")
    a = int(input("Digite 1 se for novo, caso contrário, digite 0: "))
    if a == 1:
        inscrever()
    elif a == 0:
        login()
    else:
        print("Você inseriu uma entrada incorreta!")
