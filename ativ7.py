from random import randint
eu = randint(0, 100)
print('Tente adivinhar o número que eu estou pensando!')
adivinhacao = 0
while True:
    adivinhador = int(input('Diga o número: '))
    adivinhacao += 1
    if adivinhacao == eu:
     print('PARABÉNS, VOCÊ ACERTOU O NÚMERO!')
     break

    elif adivinhador < eu:
       print('O número é maior. Tenta de novo')
    else:
       print('O número é menor. Tenta de novo')