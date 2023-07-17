import random

n1=(1, 2, 3, 4, 5)
n4=len(n1)
n3=random.choice(n1)
n2=int(input('Escolha um numero entre 1 a 5 e tente sua sorte: '))
print(f'Você escolheu {n2}')
if n2==n3:
    print(f'O numero sorteado é {n3}! PARABÉNS!!!')
else:
    print(f'O numero sorteado é {n3}! tente na proxima...')

