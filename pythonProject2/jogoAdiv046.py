import random
n1=random.choice([1, 2, 3, 4, 5])
n2=int(input('Escolha um numero de 1 á 5: '))
from time import sleep
print('PROCESSANDO...')
sleep(3)
if n1==n2:
    print('PARABÉNS VOCÊ GANHOU!!!')
else:
    print(f'MAQUINA:ESCOLHI O NUMERO {n1} EU GANHEI HAHA!!!')
    