#096-metros quadrados
'''def area(a, b):
    area=a*b
    print(f'A área de um terreno {a:.1f}x{b:.1f} é de {area:.1f}')
a=float(input('Largura (m): '))
b=float(input('Comprimento (m): '))
area (a, b)'''

#097-medida igual no texto
'''def escreva(*texto):
    quant=len(text)
    print('-'*quant)
    print(text)
    print('-' * quant)
text=str(input('Digite uma frase: '))
escreva(text)'''

#098-Pulando numeros
'''import time
def pulando(i, f, p):
    if p<0:
        p*=-1
    if p==0:
        p=1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i<f:
        cont=i
        while cont<=f:
            print(f'{cont}', end=' ')
            cont+=p
            time.sleep(0.5)
        print('Fim!')
    if i>f:
        cont=i
        while cont>=f:
            print(f'{cont}', end=' ')
            cont-=p
            time.sleep(0.5)
        print('Fim!')
pulando(1, 10, 1)
pulando(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
i=int(input('Inicio: '))
f=int(input('Fim: '))
p=int(input('Passo: '))
pulando(i, f, p)'''

#099- numeros aleatorio
'''import time
def numeros(* num):
    print('Analisando valores passados...')
    maior=cont=0
    for valor in num:
      print(f'{valor}', end=' ')
      cont+=1
      if maior<valor:
          maior=valor
      time.sleep(0.5)
    print(f'Foram informados {cont} valores, ao todo.')
    print(f'O maior valor informador é {maior}')
numeros(3, 2, 9, 4, 7, 1)
numeros(7, 3, 8)
numeros(3, 1)
numeros(2)
numeros()'''

#100-Funções para sortear e somar
import random
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        lista.append(random.randint(1, 10))
    print(numeros)
def somapares(lista):    
    soma=0
    for cada_valor in lista:
        if cada_valor%2==0:
            soma+=cada_valor
    print(f'Somando os valores pares de {lista}, temos {soma}')
numeros=[]
sorteia(numeros)
somapares(numeros)



