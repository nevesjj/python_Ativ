import ativ6
gerenciamento = ativ6.GerenciadorDeTarefas(adic = None,
                                           remov = None,
                                           feito = None,
                                           tarefas = [],
                                           tarefasFeitas = [])

op = 0
while op !=5:
    print('Digite 1: VER LISTA DE ATIVIDADES\n')
    print('Digite 2: ADICIONAR UMA ATIVIDADE\n')
    print('Digite 3: REMOVER UMA ATIVIDADE\n')
    print('Digite 4: MARCAR COMO ATIVIDADE FEITA\n')
    print('Digite 5: SAIR')
    op = int(input())

    if op == 1:
        print(f'Atividades para serem feitas: {gerenciamento.fazer}\n',
              f'Atividades concluídas {gerenciamento.tarefasFeitas}')
    #op 1
    if op == 2:
        gerenciamento.adic = input('Digite a tarefa: ')
        gerenciamento.adic = gerenciamento.adic.upper()

        if gerenciamento.adic in gerenciamento.fazer:
            print(f'Atividade {gerenciamento.adic} já existe na lista')
        else:
            gerenciamento.adicAtividade(gerenciamento.adic)
            print(f'{gerenciamento.adic} foi adicionado a sua lista')
    #op 2
    if op == 3:
        gerenciamento.remov = input('Digite a atividade ')
        gerenciamento.remov = gerenciamento.remov.upper()

        if gerenciamento.remover in gerenciamento.tarefas:
            gerenciamento.removerTarefa(gerenciamento.remov)
            print(f'{gerenciamento.remover} foi excluído da sua lista de atividades')
        else:
            print(f'A atividade {gerenciamento.remov} não existe')
    #op 3
    if op == 4:
        gerenciamento.feito = input('Digite a atividade: ')
        gerenciamento.feito = gerenciamento.feito.upper()            
        
        if gerenciamento.feito in gerenciamento.tarefas:
            gerenciamento.marcarFeito(gerenciamento.feito)
            print(f'{gerenciamento.feito} foi marcado como feito!')
        else:
            print(f'A atividade{gerenciamento.remov} não existe')
    #op 4
    if op < 1 or op > 5:
        print('Opção inválida! Tente novamente')
#while
        
            






                                           
                                           
                                           