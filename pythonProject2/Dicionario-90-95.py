#090-Dicionario python
'''dicio=dict()
dicio['nome']=str(input('Nome: '))
dicio['média']=float(input(f'Media de {dicio["nome"]}: '))
if dicio['média']<=5:
    dicio['situação']='Reprovado'
elif dicio['média']>5 and dicio['média']<7:
    dicio['situação']='Recuperação'
else:
    dicio['situação']='Aprovado'
for key, value in enumerate(dicio): #em vez de enumerate pode usar dicio.items()
    print(f'{value} é igual a {dicio[value]}')'''
#import datetime

#Jogo de dados em python
'''import random
import time
dicio={}
for cada in range(0, 4):
    dicio[f'Jogador {cada+1}']=random.randint(1, 6)
    print(f'{f"Jogador {cada+1}"} tirou {dicio[f"Jogador {cada+1}"]}')
    time.sleep(0.9)
ordenado=sorted(dicio.values(), reverse=True)
for cada, numeros in enumerate(ordenado):
    print(f'{cada+1}° lugar: {f"Jogador {cada+1}"} com {numeros}')
    time.sleep(0.7)'''

#092-Cadastro de trabalhador
'''import _datetime
dicio={}
while True:
    dicio['nome']=str(input('Nome: '))
    dicio['idade']=int(input('Ano de Nascimento: '))
    dicio['ctps']=int(input('Carteira de Trabalho (0 não tem): '))
    if dicio['ctps']==0:
        break
    dicio['contratação']=int(input('Ano de Contratação: '))
    dicio['salário']=int(input('Salário: R$'))
    dicio['idade'] = datetime.datetime.now().year - dicio['idade']
    dicio['aposentadoria'] = dicio['contratação'] + 35 + dicio['idade'] - datetime.datetime.now().year
    break
for key, value in dicio.items():
    print(f'{key} tem o valor {value}')'''

#093-Cadastro de jogador de futebol
'''dicio=dict()
gols = []
total=0
dicio['nome']=str(input('Nome do jogador: '))
n1=int(input(f'Quantas partidas {dicio["nome"]} jogou? '))
for cada in range(n1):
    n2=int(input(f'Quantos gols na partida {cada}? '))
    total += n2
    gols.append(n2)
dicio['gols']=gols
dicio['total']=total
print(dicio)
for key, value in dicio.items():
    print(f'O campo {key} tem o valor {value}')
print(f'O jogador {dicio["nome"]} jogou {n1} partidas')
for num, cada in enumerate(dicio['gols']):
    print(f'Na partida {num}, fez {cada} gols.')
print(f'Foi um total de {dicio["total"]} gols.')'''

'''#094-Unindo dicionarios e listas
lista=[]
mulheres = []
cont=0
media=0
while True:
    dicio = {}
    dicio['nome']=str(input('Nome: '))
    while True:
        dicio['sexo']=str(input('Sexo: [M/F] '))
        if dicio['sexo'].lower()=='m' or dicio['sexo'].lower()=='f':
            break
    dicio['idade']=int(input('Idade: '))
    media+=dicio['idade']
    cont+=1
    lista.append(dicio.copy())
    while True:    
        n1=str(input('Quer continuar? [S/N] '))
        if n1.lower()=='n' or n1.lower()=='s':
            break
    if n1.lower()=='n':
        break
media=media/cont
print(f'Ao todo tem {cont} pessoas cadastradas')
print(f'A média de idade é {media:.2f} anos')
for cada in lista:
    if cada['sexo'].lower()=='f':
        mulheres.append(cada['nome'])
if len(mulheres)>1:
    print(f'As mulheres cadastradas são {", ".join(mulheres)}.')
else:
    print('Não há mulheres cadastradas')
print(f'Pessoas com idade acima da media: ')
for cada in lista:
    if cada['idade']>media:
        for k, v in cada.items():
            print(f'{k} = {v}; ', end='')
        print()'''

#095-Aprimorando os dicionários
jogadores=[]
dicio={}
while True:
    gols = []
    total = 0
    dicio['nome']=str(input('Nome do jogador: '))
    n1=int(input(f'Quantas partidas {dicio["nome"]} jogou? '))
    for cada in range(n1):
        n2=int(input(f'Quantos gols na partida {cada}? '))
        gols.append(n2)
        total+=n2
    dicio['gols']=gols
    dicio['total']=total
    jogadores.append(dicio.copy())
    while True:
        n3=str(input('Quer continuar [S/N] '))
        if n3.lower()=='n' or n3.lower()=='s':
            break
    if n3.lower()=='n':
        break
for num, cada in enumerate(jogadores):
    print(f'{num} {cada["nome"]}  {cada["gols"]} {cada["total"]}')
while True:
    n3 = int(input('Mostrar dados de qual jogador? '))
    if n3>=len(jogadores):
        print(f'Digite um valor valido!')
    elif n3<len(jogadores):
        for num, cada in enumerate(dicio['gols']):
            print(f'No jogo {num+1} fez {cada} gols.')
    if n3==999:
        break 