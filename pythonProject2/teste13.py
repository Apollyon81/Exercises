"""from time import sleep
for n in range(10, -1, -1):
    print(n)
    sleep(1)"""
"""print('Os pares de 1 a 50 é')
for c in range(0, 51, 2):
    print(c)"""
"""for r in range(0, 500, 3):
    print(r)"""
"""for a in range(0, 11,):
    for b in range(0, 11):
        print(a, 'x', b, '=', a * b)"""
"""soma=0
for c in range(0, 7, 2):
    n1=int(input('Digite um numero: '))
    if n1%2==0:
        soma+=n1
print(f'A soma dos numeros pares na lista vai dar {soma}')"""

"""contador=0
for c in range(0,6):
    n1=int(input('Quantos anos você tem? '))
    if n1>18:
               contador +=1
print('São ',contador,' pessoas que tem mais que 18')"""

"""nomes=[]
for c in range(0, 4):
    n2=str(input('Qual é o seu nome: '))
    n1=float(input('Qual é o seu peso: '))
    nomes=nomes+[(n2, n1)]
peso=0    
pessoas=''  
for n2, n1 in nomes:
    if n1>peso:
        peso=n1
        pessoas=n2
    
print(f'A pessoa com maior peso é {pessoas} que pesa {peso}Kg')"""

idade=-1
nhomens=0
idades=0
maisv=''
midade=[]
mulhers=0 #numero de mulheres
for a in range(0, 3):
    n1=str(input('Qual é o seu nome: '))
    n2=int(input('Qual é a sua idade: '))
    nn2=str(input('Qual é seu genero: '))
    idades +=n2/3
    midade=midade+[(n1, n2, nn2)]
print(f'A media de idade do grupo é {idades:.0f}')
for n1, n2, nn2 in midade:
    if n2>idade and 'masculino' in nn2.lower():
        nhomens +=1
        idade=n2
        maisv=n1
    if n2>=20 and 'feminino' in nn2.lower():
        mulhers +=1
if nhomens>=1:
     print(f'O homem com a maior idade é {maisv} que está com {idade} anos')
else:
    print('Não há homens na lista')
if mulhers>=1:
    print(f'Tem {mulhers} mulher acima de 20 anos')
else:
    print('Não há mulheres na lista')
    


    





    
    
    
    
    
    


    