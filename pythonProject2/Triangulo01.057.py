n1=int(input('Medida de um lado do tringulo é: '))
n2=int(input('Medida de um lado do tringulo é: '))
n3=int(input('Medida de um lado do tringulo é: '))
if n1==n2 and n2==n3:
    print('As medidas forman um triângulo Equilátero')
elif n1==n2 or n1==n3 or n2==n3:
    print('As medidas forman um triângulo Isósceles')
elif (n1+n2)>=n3 and (n2+n3)>=n1 and (n1+n3)>=n2:
    print('As medidas forman um triângulo Escaleno')
else:
    print('Essas medidas não forman um triângulo')
    