#090
'''dicio={}
dicio['Nome']=str(input('Nome: '))
dicio['Média']=float(input('Média: '))
if dicio['Média']>=7:
    dicio['Situação']='Aprovado'
elif 5<= dicio['Média']<7:
    dicio['Situação']='Recuperação'
else:
    dicio['Situação']='Reprovado'
for key, value in dicio.items():
    print(f'{key} é igual a {value}')'''

#091-Sorteio
'''import random
import time
dicio={}
for num in range(0, 4):
    dicio[f'Jogador{num+1}'] = random.randint(1, 6)
    print(f'O jogador{num+1} tirou {dicio[f"Jogador{num+1}"]}')
    time.sleep(0.9)
ordem = dict(sorted(dicio.items(), key=lambda item: item[1], reverse=True))
for posicao, jogador in enumerate(ordem, 1):
    print(f'{posicao}° lugar: {jogador} com {ordem[jogador]}')
    time.sleep(0.9)'''

#092-Aposentadoria
'''from datetime import datetime
dicio={}
while True:
    for a in range(1):
        dicio['nome']=str(input('Nome: '))
        nasc=int(input('Ano de nascimento: '))
        dicio['idade']=datetime.now().year-nasc
        dicio['ctps']=int(input('Carteira de trabalho (0 não tem): '))
        if dicio['ctps']==0:
            break
        dicio['contratação']=int(input('Ano de contratação: '))
        dicio['salário']=float(input('Salário: R$ '))
        dicio['aposentadoria'] = dicio['idade'] + (dicio['contratação'] + 35) - datetime.now().year
    for key, values in dicio.items():
        print(f'{key} tem o valor {values}')
    break'''

#093-GOLS
'''dicio={}
gols=[]
total=0
dicio['nome']=str(input('Nome do jogador: '))
n1=int(input(f'Quantas partidas {dicio["nome"]} jogou? '))
for cada in range(n1):
    gols_partida=int(input(f'Quantos gols na partida {cada}? '))
    gols.append(gols_partida)
    total+=gols_partida
dicio['gols']=gols[:]
dicio['total']=total#pode usar sum pra fazer a soma de partidas
print(f'O jogador {dicio["nome"]} jogou {n1} partidas')
for num, value in enumerate(gols):
    print(f'Na partida {num}, fez {value} gols.')
print(f'Foi um total de {total} gols')'''

#094-cadastro de pessoas
'''quant=0
media=0
pessoas=[]
mulheres=[]
homens=[]
while True:
    dicio = dict()
    dicio['nome']=str(input('Nome: '))
    while True:
        dicio['sexo']=str(input('Sexo? [M/F] '))
        if dicio['sexo'].lower()=='m' or dicio['sexo'].lower()=='f':
            break
        else:
            print('Digite M ou F para o sexo!')
    dicio['idade']=int(input('Idade: '))
    media += dicio['idade']
    quant += 1
    pessoas.append(dicio)
    if dicio['sexo'].lower()=='f':
        mulheres.append(dicio)
    elif dicio['sexo'].lower()=='m':
        homens.append(dicio)
    n1=str(input('Deseja continuar? [S/N] '))
    if n1.lower()=='n':
        break
media=media/quant   

mulheres_acima_da_media = [mulher for mulher in mulheres if mulher['idade'] > media]
homens_acima_da_media = [homem for homem in homens if homem['idade'] > media]
if len(mulheres)==0:
    mulheres='Não há mulheres cadastradas'
print(f'-O grupo tem {quant} pessoas')
print(f'-A media de idade é {media:.2f}')
print(f'-As mulheres cadastratadas foram: {mulheres}')
print('-Lista das pessoas que estão acima da média:')
if len(homens_acima_da_media) == 0:
    homens_acima_da_media='Não há homens com idade acima da media'
    print(homens_acima_da_media)
else:
    for homens in homens_acima_da_media:
        print(f'Homem: {homens}')
if len(mulheres_acima_da_media) == 0:
    mulheres_acima_da_media='Não há mulheres com idade acima da media'
    print(mulheres_acima_da_media)
else:
    for mulheres in mulheres_acima_da_media:
        print(f'Mulher: {mulheres}')'''

#095-Jogadores
lista=[]
while True:
    dicio = {}
    dicio['nome']=str(input('Nome do jogador: '))
    n1=int(input(f'Quantas partidas {dicio["nome"]} jogou? '))
    dicio['gols']=[]
    dicio['total']=0
    for cada in range(n1):
        gols=int(input(f'Quantos gols na partida {cada}? '))
        dicio['gols'].append(gols)
        dicio['total']+=gols
    lista.append(dicio)
    while True:
        n1=str(input('Quer continuar? [S/N] '))
        if n1.lower()=='n' or n1.lower()=='s':
            break
    if n1.lower()=='n':
        break
for num, dicio in enumerate(lista):
    print(f'{num} {dicio["nome"]} {dicio["gols"]}  {dicio["total"]}')
while True:
    n1=int(input('Mostrar dados de qual jogador? '))
    if n1 >= len(lista) or n1 < 0:
        print(f'Não existe jogador com o código {n1}! Tente novamente.')
    else:
        jogador=lista[n1]
        for cada, go in enumerate(jogador['gols']):
           print(f'No jogo {cada} fez {go}')
    if n1==999:
        break
        