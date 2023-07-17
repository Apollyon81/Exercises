#Varios numeros com flags
'''n1=0
quant=0
soma=0
while True:
    n1=int(input('Digite um valor: '))
    if n1==999:
        break
    quant+=1
    soma+=n1
print(f'A quantidades de numeros foi {quant} e soma deles é {soma}')'''

#tabuada
'''n1=1
while True:
    n1=int(input('Numero da tabuada que deseja ver: '))
    if n1<0:
        break
    tab=0
    while tab<10:
       tab+=1
       print(f'{n1} x {tab} = {n1*tab}')'''

#IMPAR OU PAR
'''import random
cont=0
cotm=0
while True:
    machi = random.randint(0, 10)
    n1=str(input('Par ou Ímpar? [P/I]'))
    n2=int(input('Escolha um numero de 0 a 10: '))
    soma=n2+machi
    if soma%2==0:
        choice='PAR'
    else:
        choice='IMPAR'
    if n1.lower()[0]==choice.lower()[0]:
        cont+=1
        print(f'DEU {choice} E A MAQUINA ESCOLHEU {machi}')
        print(f'VOCÊ GANHOU {cont} VEZES')
        if cont==3:
            print('FIM DE JOGO VOCÊ GANHOU')
            break
    else:
        cotm+=1
    if cotm==1:
        print(f'DEU {choice} E MAQUINA JOGOU {machi}')
        print('GAME OVER, VOCÊ PERDEU!')
        break'''
#ANALISE DE DADOS
'''cont=0
femi=0
masc=0
while True:
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    while True:
        n1=int(input('IDADE: '))
        if n1>0:
            break
    while True:  
        n2=str(input('SEXO: '))
        if n2.lower()[0]=='f' or n2.lower()[0]=='m':
            break
    while True:
        n3=str(input('Deseja continuar? [S/N] '))
        if n3.lower()[0]=='s' or n3.lower()[0]=='n':
            break
    if n1>=18:
        cont+=1
    if n2=='f' and n1>=20:
        femi+=1
    if n2=='m':
        masc+=1
    if n3.lower()[0]=='n':
        break
print(f'Total de pessoas com mais de 18 anos: {cont}\nAo todo temos {masc} cadastrados\nE temos {femi} mulheres maiores de 20 anos')'''

#Estatisticas em produtos
'''soma=menor=totalmil=quant=0
barato = ''
while True:
    next=' '
    n1=int(input('Preço: '))
    n2=str(input('Nome do produto: '))
    quant+=1
    soma+=n1
    
    if n1 > 1000:
        totalmil += 1
    if quant==1 or n1<menor:
        menor= n1
        barato=n2    

    while next not in 'sn':
        next=str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
        break
    if next=='n':
        break

print(f'A soma de tudo deu {soma}')
print(f'Teve {totalmil} produtos acima de 1000R$')
print(f'O produto mais barato foi {barato} que custou foi {menor} ')'''

#CAIXA DE BAICO:
import random
un = vinte= cinq = 0
maqui=-1-20-50
n1 = int(input('Quanto deseja sacar? '))
while True:
    maqui = random.choice([1, 20, 50])
    if maqui == 1:
        if n1 >= 1:
            un += 1
            n1 -= 1
    elif maqui == 20:
        if n1 >= 20:
            vinte += 1
            n1 -= 20
    elif maqui == 50:
        if n1 >= 50:
            cinq += 1
            n1 -= 50
    if n1==0:
        break
print(f'DEU {un} moedas de 1R$')
print(f'Total de {vinte} cédulas de 20R$')
print(f'Total de {cinq} cédulas de 50R$')


        
        
        


        

        
    





        
    