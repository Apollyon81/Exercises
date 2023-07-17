#101 Função de votação
'''from _datetime import date
def vota(pergunta, obrig, naov, opcional):
    n1=int(input(pergunta))
    n2=date.today().year-n1
    if n2<18:
        print(f'Com {n2}:',naov)
    elif n2>=18 and n2<64:
        print(f'Com {n2} anos:',obrig)
    else:
        print(f'Com {n2} anos:',opcional)

argumentos=vota('Em que ano você nasceu? ', 'VOTO OBRIGATORIO', 'NÃO VOTA', 'VOTO OPCIONAL')'''

#102-Função para Fatorial
'''def fatorial(numeros, Show=False):
    fatoria = 1
    for cada in range(numeros, 0, -1):
        fatoria *= cada
        if Show:
            print(cada, end='')
            if cada>1:
                print(end='x')
            else:
                print('=', end='')
    return fatoria

print(fatorial(5, Show=True))'''

#103-ficha de jogador
'''def jogadores(nome='Desconhecido', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')

n1=str(input('Nome do jogador: '))
n2=str(input('Numero de gols: '))
if n1=='':
    n1='Desconhecido'
if n2=='':
    n2=0
jogadores(n1, n2)'''

#104 leia int
'''def leia(valor):
    while True:
        n1=input(valor)
        if n1.strip().isdigit():
            return n1
        else:
            print('Digite um numero inteiro valido!')

n=leia('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}')'''

#105-analisando e gerando dicionarios
'''def notas(*resp, sit=False):
    mini=min(resp)
    maxi=max(resp)
    total=len(resp)
    media=sum(resp)/total
    resp={'Total':total, 'maior':maxi, 'menor':mini, 'média':media}
    if sit:
        if media<5:
            resp['situação:']='RUIM'
        elif media<7:
            resp['situação']='BOA'
        else:
            resp['situação']='EXCELENTE'
    return resp

resp=notas(6, 1, 6.4, 7.5, 7, sit=False)
print(resp)'''

#106-sistema interativo de ajuda python
from time import sleep
c = ('\033[m',    #0- sem cores 井井
'\033[0;30;41m',  #1- vermelho
'\033[0;30;42m',  #2- verde
'\033[0;30; 43m', #3- amarelo
'\033[0;30;44m',  #4- azul
'\033[0;30; 45m', #5- roxo
'\033[7;30m',     #6- preto
'\033[47m',       #7- Fundo branco
'\033[30m',      #8- Letra preta
     )
def ajuda(msn, intro):
    while True:
        print('\033[0;30;42m')
        print('~'*(len(intro)+4))
        print(f'  {intro}  ')
        print('~' * (len(intro) + 4))
        print('\033[m')
        n1=input(msn)
        sleep(0.3)
        if n1.lower()=='fim':
            print('\033[0;30;41m')
            print('ENCERRANDO...')
            sleep(0.6)
            break
        print('\033[0;30;44m')
        print(f'ACESSANDO O COMANDO {n1}')
        print('\033[47m')
        sleep(0.6)
        print(help(n1))
he=ajuda('Função ou biblioteca: ', 'SISTEMA DE AJUDA PyHELP')


