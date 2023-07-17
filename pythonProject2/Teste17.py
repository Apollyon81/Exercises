#exemplos
'''Lista=[2, 4, 2, 3, 8, 9]
Lista[3]= 2
Lista.append(9)
Lista.sort(reverse=True)
Lista.insert(0, 9)
Lista.pop()
print(Lista)'''
'''valores=list()
for cont in range(0, 4):
    valores.append(int(input('Digite uma valor: ')))
print(valores)
for c, v in enumerate(valores):
    print(f'Na possição {c+1} encontrei o valor {v}!')'''

'''valor=[]
valor.append(1)
valor.append(3)
valor.append(9)
for c, v in enumerate(valor):
    print(f'Na possição {c+1} encontrei o valor {v}!')'''

'''lista=[]
ver=0
for cada in range(0,4):
    lista.append(int(input(f'Digite um valor para a posição {cada+1}: ')))
print(f'Você digitou os numeros, {lista}')
ver=max(lista)
menor=lista[0]
for menoor in lista:
    if menoor<menor:
        menor=menoor
print(f'O maior numero digitado é {ver}')
print(f'O menor numero digitado é {menor}')'''

#079-Adicinando somente numeros diferentes
'''lista=[]
num=[]
while True:
    numeros=int(input('Digite um numero: '))
    if numeros not in lista:
       lista.append(numeros)
    else:
        print('Valor duplicado! Não vou adicionar...')
    n1 = str(input('Deseja continuar? [S/N] '))
    if n1.lower()=='n':
        break
print(f'Você digitou os numeros {lista}')'''

#080-ordem sem sorted
'''lista=[]
for c in range(5):
    n1=int(input('Digite um numero: '))
    lista.append(n1)
    print(f'O numero {n1} foi adicionado na posição {c}')
print(f'Você digitou os valores {lista}')'''

#81-quantos e se há
'''quantia=0
lista=[]
while True:
    n2=int(input('Digite um numero: '))
    lista.append(n2)
    n1=str(input('Deseja continuar? [S/N] '))
    if n1.lower()=='n':
        break
print(f'Você digitou os numeros {lista}')
if 5 in lista:
    print('Há o numero 5 na lista')
else:
    print('Não há o numero 5 na lista')'''
    
'''#82- Crie a lista e faz+2 com impar e par
lista=[]
par=[]
impar=[]
while True:
    n1=int(input('Digite um valor: '))
    lista.append(n1)
    if n1%2==0:
        par.append(n1)
    else:
        impar.append(n1)
    n2 = str(input('Deseja continuar? [S/N]'))
    if n2.lower()=='n':
        break
print(f'Os numeros digitados são {lista}')
print(f'Os numeros pares da lista são {par}')
print(f'Os numeros impares da lista são {impar}')'''


#errado ver no futuro        
'''lista=['((', ')', '(', '))']
n1=str(input('Digite a expressão: '))
pilha=[]
for cada_simbolo in n1:
    if pilha and pilha[-1] == lista[0] and cada_simbolo == lista[1]:
        pilha.pop()
    else:
        pilha.append(cada_simbolo)
if not pilha:
    print('Sua expressão esta correta!')
else:
    print('Sua expressão está errada!')'''

    
    
        

    