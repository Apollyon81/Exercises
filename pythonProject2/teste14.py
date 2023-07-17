'''n1=''
for c in range(0, 4):
    while True:
        if 'M'.lower() and 'F'.lower() in n1:
            n1 = str(input('Qual é o seu seu M/F: '))
        else:
            print('Digite se é M ou F')'''
import sys

#SORTEIO
'''import random
while True:
    chances = 0
    acertou = False
    n1 = random.randint(0, 10)
    while not acertou:
        n2=int(input('Digite um numero de 1 á 10:'))
        chances+=1
        if n1==n2:
           print(f'A maquina escolheu {n1}, Você acertou!') 
           print(f'Você teve {chances} palpites para acertar!')
           acertou = True
           
    resposta=str(input('Deseja continuar Y/N: '))
    if resposta.lower()=='n':
        break'''

'''#OPÇÕES
while True:
    n1=int(input('Escolha o primeiro valor: '))
    n2=int(input('Escolha o segundo valor: '))
    n3=int(input('VOCÊ DESEJA:\n[1]somar\n[2]multiplicar\n[3]novos números\n[4]sair do programa\nSua opção: '))
    if n3==1:
        resu=n1+n2
        print(f'A soma de {n1} e {n1} é {resu}')
    elif n3==2:
        resu=n1*n2
        print(f'A multiplicação de {n1} e {n2} é {resu}')
    elif n3==3:
        continue
    elif n3==4:
        print('Fim da operação')
        break
    else:
        print('Digite uma opção valida')'''

#Fatorial
'''n1=int(input('Digite um numero e dire seu fatorial: '))
fatorial=1
nume=''
n2=n1
while n1>=1:
        fatorial*=n1
        nume+=str (n1)
        if n1>1:
                nume+='x'[::-1]
        n1-=1
print(f'{n2}!={nume}={fatorial}')'''

'''#PA
n1=int(input('Qual é termo? '))
n2=int(input('Qual é a razão? '))
n3=int(input('Quantos termos você deseja ver? '))
atual=n1
cont=1
while cont<=n3:
    sep='-->' if cont<n3 else ''
    print(atual, sep, end='')
    atual+=n2
    cont+=1
    
while True:
    n4 = str(input(f'\nQuer vendo mais termos? Y/N? '))
    if n4.lower()=='n':
        break
    elif n4.lower()=='y':
        n5=int(input('Quantos termos a mais você quer ver: '))
        atual = n1 + (cont - 1) * n2
        for c in range(n5):
            atual+=n2
            sep = '-->' if c < n5-1 else ''
            print(cont, sep, end='')
            cont +=1
print('\nFIM DO PROGRAMA!')'''

#Até acertar
'''nume=0
soma=0
while True:   
    n1=int(input('Digite um numero: '))
    if n1==999:
        break
    else:
        nume+=1
        soma+=n1
print(f'A quantidades de numeros foi {nume} e a soma deles é {soma}')'''

#media de numeros
soma=0
media=0
maior=0
menor=sys.maxsize
nume=0
while True:
    n1=int(input('Digite um numero: '))
    soma+=n1
    nume+=1
    if n1>maior:
        maior=n1
    if n1<menor:
        menor=n1
    n2=str(input('Deseja continuar? Y/N '))
    if n2.lower()=='n':
        break
    elif n2.lower()=='y':
        continue
    else:
        print('Digite uma opção valida')
if nume>0:
    media+=soma/nume
print(f'A media dos numero é {media} o maior foi {maior} e o menor foi {menor}')
    
        
    


        
    
       
       




