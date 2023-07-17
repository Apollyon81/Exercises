a=float(input('Digite a primeira medida: '))
b=float(input('Digite a segunda medida: '))
c=float(input('Digite a terceira medida: '))
if a+b>c and a+c>b and b+c>a:
    print('As medidas formam um triangulo')
else:
    print('As medidas não formam um triangulo')