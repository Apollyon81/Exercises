#084-Listas composta e analise de dados
'''lista=[]
nomes=[]
nomesl=[]
pesado=0
leve=float('inf')
while True:
    nome=str(input('Nome: '))
    peso=float(input('Peso: '))
    lista.append([nome, peso])
    n1=str(input('Deseja continuar? [S/N] '))
    if n1.lower()=='n':
        break
for cada in lista:
    if cada[1]>pesado:
        pesado=cada[1]
        nomes=[cada[0]]
    elif cada[1]==pesado:
        nomes.append(cada[0])
    if cada[1]<leve:
        leve=cada[1]
        nomesl=[cada[0]]
    elif cada[1]==leve:
        nomesl.append(cada[0])
print(f'Foram {len(lista)} pessoas')
print(f'O mais pesado foi de {pesado}kilos. peso de {", ".join(nomes)}')
print(f'O mais leve tem {leve}Kilos. peso de {", ".join(nomesl)}')'''
import random

#Teste do 84
'''temporaria=[]
principal=[]
maior=menor=0
while True:
    temporaria.append(str(input('Digite o nome: ')))
    temporaria.append(float(input('Peso: ')))
    if len(principal)==0:
        maior=menor=temporaria[1]
    else:
        if temporaria[1]>maior:
            maior=temporaria[1]
        if temporaria[1]<menor:
            menor=temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()
    resp=str(input('Quer continuar? '))
    if resp.lower() in 'n':
        break
print(principal)
print(f'Foram {len(principal)} pessoas')
        
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for pessoas in principal:
    if pessoas[1]==maior:
        print(f'[{pessoas[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for pessoas in principal:
    if menor==pessoas[1]:
        print(f'{pessoas[0]}', end=' ')
print()'''

#085-Listas com pares e impares
'''lista=[[], [], []]
for pergunta in range(7):
    lista[0].append(int(input(f'Digite o {pergunta+1}. valor: ')))
for cada in lista[0]:
    if cada%2==0:
        lista[1].append(cada)
    else:
        lista[2].append(cada)
print(f'Os pares são {lista[1]}')
print(f'Os impares são {lista[2]}')'''
#usando 1 lista com somente 2 listas dentro
'''lista=[[], []]
for pergunta in range(0, 7):
    n1=int(input(f'Digite o {pergunta+1}. valor: '))
    if n1%2==0:
        lista[0].append(n1)
    else:
        lista[1].append(n1)
print(f'Os pares são {sorted(lista[0])}')
print(f'Os impares são {sorted(lista[1])}')'''

#086-Matriz em python
'''lista=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for numeros in range(0,3):
    for cada in range(0,3):
         lista[numeros][cada]=int(input(f'Digite um numero para {numeros} {cada}: '))
for numeros in range(0,3):
    for cada in range(0,3):
        print(f'{[lista[numeros][cada]]}', end='')
    print()'''

#087-Mais sobre matrizes
'''lista=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares=0
soma=0
maior=0
for c in range(3):
    for n in range(3):
        lista[c][n]=int(input(f'Para {c} {n}. Digite um numero: '))
for c in range(0,3):
    for n in range(0,3):
        print([lista[c][n]], end='')
        if lista[c][n]%2==0:
            pares+=lista[c][n]
    print()
for c in range(3):
    soma+=lista[c][2]
for cada in lista[1]:
    if cada>maior:
        maior=cada
        
print(f'A soma dos pares é {pares}')
print(f'A soma da terceira coluna é {soma}')
print(f'O maior numero numero na segunda coluda é {maior}')'''

#088-telecena
'''from random import randint
import time
lista=[0, 0, 0, 0, 0, 0]
cont=0
n1=int(input('Você quer ver quantos jogos? '))
while cont<n1:
    for cada in range(len(lista)):
        lista[cada]=randint(0, 60)
    cont+=1
    print(lista)
    time.sleep(0.7)'''

#089-Boletin com listas
'''lista=[]
while True:
    nome=str(input('Nome: '))
    nota1=float(input('Nota 1: '))
    nota2=float(input('Nota 2: '))
    media=(nota1+nota2)/2
    lista.append([nome,[nota1, nota2],media])
    n1=str(input('Deseja continuar? [S/N] '))
    if n1.lower()=='n':
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}:')     
for nu, cada in enumerate(lista):
    print(f'{nu:<4}{cada[0]:<10}{cada[2]:>8}')
while True:
    n2=int(input('Deseja ver as notas de qual aluno? (999 Interrompe): '))
    for nu, cada in enumerate(lista):
        if n2==nu:
            print(f'Aluno: {cada[0]} notas: {cada[1]}')
    if n2==999:
        break'''

        