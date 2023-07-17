"""from time import sleep
for cont in range(10, -1, -1,):
    print(cont)
    sleep(1)
print('BUUM--POWW')"""
"""for c in range(2, 51, 2):
    print('..', end='')
    print(c, end=' ')
print('ACABOU')"""

"""soma=0
contador=0
for c in range(1, 501, 2):
    if c % 3==0:
      soma=soma+c
      contador+=1
print(f'A soma do multiplo de 3 de 500 é {soma} no total de {contador} valores')"""

#tabuada
"""n1=int(input('Digite um numero para ver sua tabuada: '))
for c in range(0, 11):
    print(f'{n1}x{c} =', n1*c)"""

#Soma de pares
'''cont=0
soma=0
for c in range(6):
    n1=int(input('Digite um numero: '))
    if n1%2==0:
       soma+=n1
       cont+=1
print(f'Tem {cont} numeros pares e a soma deles é {soma}')'''

#progressão aritmética
'''razao=0
n1=int(input('Qual é o primeiro termo: '))
n2=int(input('Qual é a razão: '))
for c in range(10):
    razao=n1+n2*c
    sep='-->'if c<9 else ''
    print(f'{razao}{sep}', end='')'''

'''contador=0
n1=int(input('Digite um numero: '))
for c in range(1, n1 + 1):
    if n1%c==0:
        print('\033[31m', end=' ')
        contador+=1
    else:
        print('\033[33m', end=' ')
    print(f'{c}', end=' ')
if contador==2:
    print(f'\n\033[m{n1} é divisivel por {contador} portanto é um numero primo')
else:
    print(f'\n\033[m{n1} Não é numero primo')'''

#poligramo
'''n1=input('Diga uma frase: ').strip().lower()
word=n1.split()
junto=''.join(word)
inverso=junto[::-1]
if junto==inverso:
    print(f'A palavra {n1} é um poligramo')
else:
    print(f'A palavra {n1} não é um poligramo')'''

#Grupo de maioridade
'''from _datetime import date
contma=0
contame=0
for c in range(1, 6):
    n1=int(input(f'Em que ano nasceu a {c}° pessoa?  '))
    n2 = date.today().year
    n3=n2-n1
    if n3>=18:
        contma+=1
    elif n3<18:
        contame+=1
print(f'Ao todo tivemos {contma} pessoas maior de idade')
print(f'E tivemos {contame} pessoas menor de idade')'''

#medindo peso
'''peso=0
pesom=1000
for c in range(5):
    n1=float(input('Qual é o seu peso: '))
    if n1>peso:
        peso=n1
    if n1<pesom:
        pesom=n1
print(f'A pessoa mais pesada tem {peso:.1f}Kg')
print(f'E a pessoa com o menor peso tem {pesom:.1f}Kg')'''
media=0
Nmulher=0
mulher=0
maior=0
nomeh=''
for c in range(0, 4):
    nome=str(input('Qual é o seu nome: '))
    gen=str(input('Qual é seu genero: '))
    idade=int(input('Qual é a sua idade: '))
    media+=idade/4
    if idade>maior and 'masculino' in gen.lower():
        maior=idade
        nomeh=nome
    if gen.lower() in 'feminino' and idade>=20:
        Nmulher+=1
        
print(f'O homem com mais velho é {nomeh} que está com {maior} anos')
print(f'A media de idade do grupo é {media:.0f} anos')
print(f'Tem {Nmulher} mulher com maior de 20 anos')





        
    



    
    

    
    
    
    
