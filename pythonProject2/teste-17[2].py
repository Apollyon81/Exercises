#exemplo
'''galera=list()
dado=list()
for cada_pessoa in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)'''

#084-Pessoas mais leves e mais pesadas
'''dados=[]
nomem=[]
maior=0
menor=float('inf')
while True:
    lista = []
    lista.append(str(input('Nome: ')))
    lista.append(int(input('Idade: ')))
    if lista[1]>maior:
        maior=lista[1]
        nomem=[lista[0]]
    elif lista[1]==maior:
        nomem.append(lista[0])
    if lista[1]<menor:
        menor=lista[1]
    dados.append(lista[:])
    n1=str(input('Deseja continuar? [S/N] '))
    if n1.lower()=='n':
        break 
print(f'Tem {len(dados)} pessoas cadastradas')
print(f'O mais velho/a é {", ".join(nomem)} que tem {maior} anos')
print(f'A pessoa mais nova tem {menor}')'''
#085-PARES E IMPARES
'''princi=[]
par=[]
impar=[]
for cada in range(0,7):
    princi.append(int(input(f'Digite o {cada+1} numero: ')))
for cada in princi:
    if cada%2==0:
        par.append(cada)
    else:
        impar.append(cada)
par.sort()
impar.sort()
print(f'Os numeros pares são {par}')
print(f'Os numero impares são {impar}')'''

#087-MATRIZ
'''pares=0
matriz=[[0,0,0], [0,0,0],[0,0,0]]
maior=0
for cada in range(0, 3):
    for cadas in range(0, 3):
        matriz[cada][cadas]=int(input(f'Digite um numero para {cada}, {cadas}: '))
for cada_n in matriz:
    for num in cada_n:
        if num%2==0:
             pares+=num

for cada in matriz[1]:
    maior=max(matriz[1])
               
for cada in range(0, 3):
    for cadas in range(0, 3):
        print(f'[{matriz[cada][cadas]}]', end='')
    print()
soma=matriz[2][0]+matriz[2][1]+matriz[2][2]
print(f'A soma da terceira coluna é {soma}')
print(f'A soma dos pares é {pares}')
print(f'O maior valor na segunda linha é {maior}')'''

#088 mega-sena
'''from random import randint
jogos=[]
tot=0
n1=int(input('Quantos jogos voce quer que eu sorteie? '))
while tot<n1:
    lista = []
    cont = 0
    while True:
        n2=randint(0, 60)
        if n2 not in lista:
            lista.append(n2)
            cont+=1
        if cont>=6:
            break
    tot+=1        
    jogos.append(lista)

for c, cada in enumerate(jogos):
    print(f'O jogo {c+1} é: {cada}')'''

#teste 89
'''lista=[]
while True:
    name=str(input('Digite seu nome: '))
    nota1=float(input('Nota 1: '))
    nota2=float(input('Nota 2: '))
    media=(nota1+nota2)/2
    lista.append([name, [nota1, nota2], media][:])
    n1=str(input('Deseja continuar? [S/N] '))
    if n1.lower()=='n':
        break       
for nu, cada in enumerate(lista):
    print(f'{nu+1}  {cada[0]}  {cada[2]}')
while True:
    n2=int(input('Quer mostra a nota de qual aluno? '))
    if n2==999:
        print('Finalizando...')
        break
    if n2<=len(lista)-1:
        print(f'Notas de {lista[n2-1][0]} são {lista[n2-1][1]}')'''
         


