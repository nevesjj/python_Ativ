n1 = float(input('Digite a nota 1 : '))
n2 = float(input('Digite a nota 2 : '))
n3 = float(input('Digite a nota 3 : '))
media = (n1+n2+n3)/3

if media <= 10 and media >= 9 :
    print('A = ',(media))
elif media <= 8 and media >= 7:
    print('B = ',(media))
elif media <= 6 and media >= 5:
    print('C = ',(media))
elif media <= 4 and media >= 3:
    print('D = ',(media))
elif media <= 2 and media >= 1:
    print('F = ',(media))
elif media == 0:
    print('Sua média foi 0')



