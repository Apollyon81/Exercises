n1=int(input('Digite um numero: '))
n2=int(input('Digite um numero: '))
n3=int(input('Digite um numero: '))
#verificando qual é o menor
menor=n1
if n2 < n1 and n2 < n3:
    menor=n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'O menor valor digitado foi {menor}')
#verificando o maior
maior=n1
if n2 > n1 and n2 > n3:
    maior=n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O maior numero foi {maior}')
    

    



