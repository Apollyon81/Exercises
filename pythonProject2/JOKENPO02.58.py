import random
from time import sleep
print('Suas opções:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA')
human=int(input('Qual é a sua jogada? '))
n1=random.randint(0,2)
print('JO')
sleep(0.9)
print('KEN')
sleep(0.9)
print('PO!!!')
sleep(0.6)
if n1==0:
    joke='PEDRA'
if n1==1:
    joke='PAPEL'
if n1==2:
    joke='TESOURA'
if human==n1:
    print(f'Computador jogou {joke}\nEMPATE!!!')
elif n1==0 and human==1:
    print(f'Computador jogou {joke}\nVOCÊ GANHOU!!!')
elif n1==1 and human==2:
    print(f'Computador jogou {joke}\nVOCÊ GANHOU!!!')
elif n1==2 and human==0:
    print(f'Computador jogou {joke}\nVOCÊ GANHOU!!!')
else:
    print(f'Computador jogou {joke}\nVOCÊ PERDEU!!!')
    

    
