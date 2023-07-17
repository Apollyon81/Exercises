#numeros
'''numeros=['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'trese', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte']
n1 = int(input('Escolha um numero de 0 á 20: '))
while n1<0 or n1>20:
        n1=int(input('Tente novamente. Escolha um numero de 0 á 20: '))
        if n1>0 and n1<20:
            break
print(f'O numero que você escolheu é {numeros[n1]}')'''

#posições times
'''colocacao=('Botafogo', 'Fortaleza', 'Palmeiras', 'Internacional', 'Fluminense', 'Cruzeiro', 'Grêmio', 'São Paulo', 'Vasco')
texto=', '.join(colocacao)+'.'
print(texto)
texto1=', '.join(colocacao[:4])+'.'
print('Os 4 primeiros colocados são ', ' '.join(texto1.split()[:4]))
texto2=', '.join(colocacao[5:])
print('Os 4 ultimos são', texto2, end='.''\n')
ordem=sorted(colocacao)
texto3=', '.join(ordem)+'.'
print('Em ordem alfabetica:', (texto3))
print(colocacao[4], f'esta na posição', colocacao.index('Fluminense')+1)'''

#SORTEIO TUPLA
'''import random
decimal=('1', '2', '3', '4', '5', '6', '7', '8', '9')
machi=random.choice(decimal)
machi1=random.choice(decimal)
machi2=random.choice(decimal)
machi3=random.choice(decimal)
machi4=random.choice(decimal)
print(machi, machi1, machi2, machi3, machi4)
valor=str(machi+ machi1+ machi2+ machi3+ machi4)
cres=sorted(valor)
adm=''.join(cres[4:])
adm1=''.join(cres[:1])
print(f'O maior valor sorteado foi {adm}')
print(f'O menor numero foi {adm1}')'''

#Posições
'''n1=int(input('Digite um numero: '))
n2=int(input('Digite outro numero: '))
n3=int(input('Digite mais um numero: '))
n4=int(input('Digite o ultimo numero: '))
tupl=(n1, n2, n3, n4)
print(f'Você digitou os numero {tupl}')
cont=tupl.count(9)
print(f'O nove aparece {cont} vezes')
par=len([x for x in tupl if x%2==0])
print(f'Os numero pares apareceu {par} vezes ')
par = [x for x in tupl if x % 2 == 0]
print(f'E eles são o numero {par}')
if 3 in tupl:
    posicao=tupl.index(3)
    print(f'O numero tres foi escolhido na {posicao+1}°')
else:
    print('O numero 3 não foi digitado')'''

#listagem de preços
'''lista=('Remedio', 2, 'Agua', 2.5, 'Batata', 4, 'Pepino', 3, 'Ameixa', 8.90)
print('LISTAGEM DE PREÇOS\n')
print('-'*38)
print(f'{lista[0]:.<28}R${lista[1]:>7.2f}')
print(f'{lista[2]:.<28}R${lista[3]:>7.2f}')
print(f'{lista[4]:.<28}R${lista[5]:>7.2f}')
print(f'{lista[6]:.<28}R${lista[7]:>7.2f}')
print(f'{lista[8]:.<28}R${lista[9]:>7.2f}')'''

#VOGAIS
palavras=('Laranja', 'Abacata', 'Amora', 'Ameixa', 'Brasilia', 'Google', 'Paralelepipedo')
vogais='a', 'e', 'i', 'o', 'u'
for vogal in palavras:
    lista=[]
    for letra in vogal:
        if letra.lower() in vogais:
            lista.append(letra.lower())
    print(f"A vogais da palavra {vogal.upper()} é:+ {', '.join(lista)}")






    




       