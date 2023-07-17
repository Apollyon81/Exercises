#78-Maior e menor valores da lista
'''lista=[]
for cada in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {cada+1}: ')))
mas=max(lista)
min=min(lista)
print(f'O maior valor da lista é {mas} que esta na posição {}')
print(f'O menor valor da lista é {min}')'''

#79-Valores únicos em uma lista
'''lista=[]
while True:
    n1=int(input('Digite um numero: '))
    if n1 in lista:
        print('Digite um valor unico!')
    else:
        lista.append(n1)
    n2=str(input('Deseja continuar? [S/N] '))
    if n2.lower()=='n':
        break
lis=sorted(lista)
print(f'Você digitou os valores {lis}')'''

#080-Lista ordenada sem repetição
'''lista=[]
for c in range(0,5):
    n1 = int(input('Digite um numero: '))
    if c==0 or n1>lista[-1]:
        lista.append(n1)
    else:
        pos=0
        while pos< len(lista):
            if n1<lista[pos]:
                lista.insert(pos, n1)
                break
            pos+=1    
print(lista)'''

#081-Extraindo dados de uma lista
'''lista=[]
while True:
    n1=int(input('Digite um numero: '))
    lista.append(n1)
    n2=str(input('Deseja continuar? [S/N] '))
    if n2.lower()=='n':
        break
lista.sort(reverse=True)
print(f'Os numeros são {lista}')
if 5 in lista:
    print('Tem o numero 5 na lista')
else: 
    print('Não há o numero 5 na lista')'''

#082-Dividindo valores em varias listas
lista=[]
par=[]
impar=[]
while True:
    n=(int(input('Didite um numero: ')))
    lista.append(n)
    if n%2==0:
       par.append(n)
    else:
        impar.append(n)
    n1 = str(input('Quer continuar [S/N] '))
    if n1.lower() == 'n':
        break
print(f'Os numeros são {lista}')
print(f'OS pares de lista são {par}')
print(f'Os impares da lista são {impar}')