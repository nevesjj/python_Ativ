print('*******CAIXA ELETRONICO*******')
print('1. DEPOSITAR')
print('2. SACAR')
print('3. SALDO')
print('4. SAIR') 
while True:
    
    opc = int(input('Digite a opção desejada: ')) 
    if opc == 1:
        dep = float(input('Digite o valor que deseja depositar: '))
        dep = float("{:.2f}".format(dep))
        print(dep)

    elif opc == 2:
        saque = float(input('Digite o valor que deseja sacar: '))
        saldo = dep - saque
        saldo = float("{:.2f}".format(saldo))
        print(saldo)

    elif opc == 3:
        saldo = float("{:.2f}".format(saldo))
        print(saldo)

    elif opc == 4:
        print('Você finalizou seu atendimento! ')
        break

    else:
        print('Opção inválida')