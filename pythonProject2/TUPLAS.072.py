#numeors por extenso
'''ate=('Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete')
while True:
    n1 = int(input('Digite um numero de 1 á 7: '))
    if 0<=n1<=7:
        print(f'O numero que você escolheu é {ate[n1 - 1]}')
    else:
        print('Digite um numero valido')
        continue
    n3 = str(input('Deseja continuar? [S/N] '))
    if n3.lower()[0]=='s':
        continue
    if n3.lower()[0]=='n':
        break'''

#import random
#Campeonato
'''fute=('Botafogo - RJ', 'Palmeiras - SP', 'Cruzeiro Saf - MG', 'Fortaleza CE', 'São Paulo - SP', 'Fluminense - RJ', 'Grêmio - RS', 'Internacional - RS', 'Bahia - BA')
print(f'Os 3 primeiros são {fute[0:3]}')
print(f'Os utimos 3 são {fute[6:9]}')
print(f'Em ordem afabetica: {sorted(fute)}')
print(f'O Palmeiras esta na posição {fute.index("Palmeiras - SP")+1}°')'''

#MENOR E MAIOR EM TUPLA
'''import random
nume=(1, 2, 3, 4, 5, 6, 7, 8, 9)
machi=random.sample(nume, 5)
print(machi)
menor=machi[0]
maior=machi[0]
for num in machi:
    if num>maior:
        maior=num
    if num<menor:
        menor=num
print(f'O menor numero foi {menor}')
print(f'O maior numero foi {maior}')'''

'''from random import randint
n=(randint(1, 10),randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ')
print(f'{n}\n', end='')
print('O maior valor foi', max(n))
print('O menor valor foi', min(n))'''

#Analize de danos em tupla
'''nume=(int(input('Digite um numero: ')),int(input('Digite o segundo numero: ')),int(input('Digite o terceiro numero: ')),int(input('Digite o ultimo numero: ')))
print(f'Você digitou os numero {nume}')
print(f'O numero 9 apareceu ',nume.count(9),'vezes')
if 3 in nume:
    print(f'O numero 3 apareceu na posição {nume.index(3)+1}')
else:
    print('Não foi digitado nenhum numero 3')
print('os valores pares digitados foram ', end='')
for cada in nume:
    if cada%2==0:
        print(cada, end=' ')'''
'''print('-'*35)
print('LISTAGEM DE PREÇOS')
print('-'*35)
tupla=('Batata', 2, 'Romã', 3.3, 'banana', 114.7, 'leite', 4.9)
for itens in range(0, len(tupla)):
    if itens%2==0:
        print(f'{tupla[itens]:.<30}', end='')
    else:
        print(f'R${tupla[itens]:>4.2f}')'''

#contando vogais
tupla=('Abacate', 'Limao', 'Banana', 'Palelepipedo', 'Programar')
vogais='a', 'e', 'i', 'o', 'u'
for p in tupla:
    print(f'\nNa palabra {p.upper()} temos,', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
