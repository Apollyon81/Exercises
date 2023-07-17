#096-medidas
'''def medida(l, c):
    a=l*c
    print(f'A area do terreno {l:.1f}x{c:.1f} é de {a:.2f}')
l=float(input('Largura (m): '))
c=float(input('Comprimento (m): '))
medida (l, c)'''
import random

#097-Um print especial
'''def escreva(texto):
    quant=len(texto)
    quant='-'*quant
    print(quant)
    print(texto)
    print(quant)
texto=str(input('Digite um texto: '))
escreva(texto)'''

#098-Função de contador
'''from time import sleep
def contador(i, f, p):
    cont = i
    if p<0:
        p*=-1
    if p==0:
        p=1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i<f:
        while cont<=f:
            print(f'{cont}', end=' ')
            cont+=p
            sleep(0.4)
        print()
    elif i>f:
        while cont>=f:
            print(f'{cont}', end=' ')
            cont-=p
            sleep(0.4)
        print()
contador(1, 10, 1)
contador(10, 0, 2)
i=int(input('Inicio: '))
f=int(input('Fim: '))
p=int(input('Passo: '))
contador(i, f, p)'''

#099-Função que descobre o maior
'''from time import sleep

def numeros(*num):
    maior=0
    lista=[]
    for cada in range(len(num)):
        cada=random.randint(0, 10)
        if cada>maior:
            maior=cada
        print(cada, end=' ')
        sleep(0.3)
        lista.append(str(cada))
    if not num:
        lista.append('0')
    print(f'Foram informados {len(lista)} ao todo')
    print(f'O maior valor informado foi {maior}')

numeros("a", "b", "c", "d", "f", "g")
numeros("a", "b", "c")
numeros("a", "b")
numeros("a")
numeros()'''

#100-Funções para sortear e somar
def numeros(n1):
    print(f'Foram sorteado {n1} valores da lista: ', end='')
    soma = 0
    lista = []
    for cada in range(n1):
        cada=random.randint(1, 10)
        if cada%2==0:
            soma+=cada
        lista.append(cada)
        print(cada, end=' ')
    print('PRONTO!')
    print(f'Somando os valores pares de {lista}, temos {soma}')
n1=int(input('Deseja sortear quantos numeros? '))
numeros(n1)
        