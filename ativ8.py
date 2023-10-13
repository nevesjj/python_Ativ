while True:
    print('*******CALCULADORA DE IMC*******')
    peso = float(input('Digite o seu peso em kg: '))
    altura = float(input('Digite sua altura em metros: '))
    imc = peso / (altura ** 2)
    print('Seu IMC é: {:.2f}'.format(imc))
    
    if imc < 18.5:
        print('Você está em situação de MAGREZA')
    
    elif imc >= 18.5 and imc <= 24.9:
        print('Você está em situação NORMAL')
    
    elif imc >= 25 and imc <= 29.9:
        print('Você está em situação de SOBREPESO')

    elif imc >= 30 and imc <= 34.9:
        print('Você está em situação de OBESIDADE GRAU 1')
    
    elif imc >= 35 and imc <= 39.9:
        print('Você está em situação de OBESIDADE GRAU 2')

    else:
        print('Você está em situação de OBESIDADE GRAU 3')
    
