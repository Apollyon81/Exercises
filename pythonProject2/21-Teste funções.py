#101- Votos
'''from _datetime import date
def ano(n1):
    n2=date.today().year-n1
    if n2<18:
        return f'Com {n2} anos: NÃO VOTA'
    elif n2>=18 and n2<65:
        return f'Com {n2} anos: VOTO OBRIGATORIO.'
    else:
        return f'Com {n2} anos: VOTO OPCIONAL.'

n1=int(input('Em que ano você nasceu? '))
print(ano(n1))'''

#102-Fatorial
'''def fatorial(num, show=False):
    total=1
    for cada in range (num, 0, -1):
        if show:
            print(cada, end=' ')
            if cada>1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        total*=cada
    return total

print(fatorial(6, show=True))'''

#103-Falso ou True para jogador
'''def pessoa(j='<Desconhecido>', g=0):
    print(f'O jogador {j} fez {g} no campeonato')
j = input('Nome do jogador: ')
g = input('Número de Gols: ')
if j.strip()=='':
    j='<Desconhecido>'
if g.strip()=='' or not g.isdigit():
    g=0
pessoa(j, g)'''

#104- Leia
'''def leia(n):
    while True:
        c=input(n)
        if c.strip().isdigit():
            return c
        else:
            print(f'\033[0;31mERRO! Digite um número inteiro válido: \033[m')

b=leia('Digite um numero: ')
print(f'Você acabou de digitar o numero {b}')'''

#105-notas
'''def leia(*msn, sit=False):
    total=len(msn)
    media=sum(msn)/len(msn)
    maior=max(msn)
    menor=min(msn)
    lista={'Total': total, 'maior': maior, 'menor': menor, 'media': media}
    if sit:
        if media>5 and media<7:
            lista['Situação:']= 'Boa'
        if media<5:
           lista['Situação:']='Ruim'
        if media>=7:
            lista['Situação:']= 'Excelente'
    return lista
resp=leia(3.5, 9, 6.5, sit=True)
print(resp)'''

#106-HELP
'''import time
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
def hel(meco, msn, msm, fin):
    while True:
        print(f'{c[2]}')
        print('~'*(len(meco)+4))
        print(f' {meco} ')
        time.sleep(0.6)
        print('~' * (len(msn)+4))
        print(c[0])
        oi=input(f' {msn} ')
        time.sleep(0.3)
        if oi.lower()=='fim':
            print(c[1])
            print('~'*(len(fin)+4))
            print(f'  {fin}  ')
            print('~' * (len(fin) + 4))
            time.sleep(0.3)
            break
        print(c[4])
        print('~'*(len(msn+oi)+4))
        print(msm, oi)
        print('~' * (len(msn + oi) + 4))
        print(c[7], c[8])
        time.sleep(0.6)
        print(f'{help(oi)}')
        time.sleep(0.6)

n1=hel('SISTEMA DE AJUDA PyHELP', 'Função ou Bibiblioteca> ', 'Acessando o manual do comando', 'ATÉ LOGO !')'''

