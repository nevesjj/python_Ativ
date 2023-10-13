palavra = 'cloves'
chances = 3
letra_certa = []
ganhou = False

while True:
    for letra in palavra:
        if letra.lower in letra_certa:
            print(letra, end=" ")
        else:
            print("", end=" ")
    print(" ")
    tentativa = input("Diga uma letra para adivinhar: ")

    letra_certa.append(tentativa.lower())
    if tentativa.lower() not in palavra.lower():

        chances -= 1

    ganhou = True
    for letra in palavra:
        if letra.lower() not in letra_certa:
            ganhou = False

    if chances == 0 or ganhou:
        break 

if ganhou:
    print(f'Parabéns, você conseguiu. A palavra era:{palavra}') 
else:
    print(f'Você perdeu! a palavra era: {palavra}')