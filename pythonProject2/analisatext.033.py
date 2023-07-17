nome=str(input('Digite seu nome: '))
n1=nome.upper()
n2=nome.lower()
no=nome.replace(' ', '')
n3= len(no)
n4=nome.split()
n5=n4[0]
n6=len(n5)

print(f'Seu nome em maiúsculo é {n1}')
print(f'Seu nome em minusculo é {n2}')
print(f'Seu nome tem {n3} Letras')
print(f'Seu primeiro nome é {n5} e tem {n6} Letras')

