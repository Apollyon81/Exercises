'''soma=0
count=-1
while True:
    n1 = int(input('Digite um numero: '))
    count+=1
    soma+=n1
    if n1==999:
        break
print(f'Foram {count} numeros e a soma dos numeros deu {soma-999}')'''
import random

#Tabuada
'''while True:
    n1 = int(input('Quer ver tabuada de qual valor: '))
    if n1 <0:
        break
    cont=0
    while cont<10:
        cont+=1
        print(f'{n1}x{cont}={n1 * cont}')'''

#par ou impar
'''from random import randint
cont=0
ga=''
cont2=0
print('VAMOS JOGAR PAR OU ÍMPAR')
while cont<3:
    cho = random.randint(0, 10)
    n1 = str(input('Escolha: [I/P] ')).lower()[0]
    n2=int(input('Escolha um numero: '))
    pi=n2+cho
    if pi%2==0:
        ga='PAR'
    elif pi%2==1:
        ga='IMPAR'
    print(f'DEU {ga} A MAQUINA ESCOLHEU {cho}')
    if n1==ga.lower()[0]:
        cont += 1
        cont2 = 0
        if cont<3:
           print(f'VOCÊ GANHOU {cont}!')
        if cont==3:
            print(f'VOCÊ GANHOU {cont} PARABENS!!!')
            break
    else:
        cont2+=1
        cont=0
        print(f'A MAQUINA GANHOU {cont2} VEZES')
        if cont2==3:
            print(f'GAME OVER, A MAQUINA GANHOU {cont2} VEZES!')
            break'''

#COMPRAS
'''quant=0
proc=''
prob=''
soma=0
maic=0
maib=0
mil=0
while True:
    n1=str(input('Qual é o nome do produto '))
    n2=int(input('Qual é o valor do produto: '))
    n3 = str(input('Deseja continuar: [S/N] '))
    if n3 == 'n'.lower()[0]:
        break
    quant+=1
    soma+=n2
    if n2>maic:
        proc=n1
        maic=n2
    if n2<maib:
        prob=n1
        maib=n2
    if n2>=1000:
        mil+=1
    else:
        continue
print(f'Teve {mil} produtos mais de Mil reais, o total foi de {soma}reais\n e o produto mais caro foi {proc} e seu valor é de {maic} reais')'''
    
#SAQUE
import random
uno=0
vin=0
cinc=0
maqui=0
n1=int(input('Quantos você deseja sacar: '))
while True:
    maqui=random.choice([1, 20, 50])
    if maqui==1:
        uno+=1
    elif maqui==20:
        vin+=1
    elif maqui==50:
        cinc+=1
    if uno * 1 + vin * 20 + cinc * 50 >= n1:
        break
        
print(f'Foram escolhidos \n{uno} notas de 1R$\n {vin} de 20R$\n{cinc} notas de 50R$')

    
        
    
        
    
    
    

