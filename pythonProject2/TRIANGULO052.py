print('=='*20)
print('Analisador de traingulos')
print('=='*20)
t1=int(input('Digite a primeira medida: '))
t2=int(input('Digite a segunda medida: '))
t3=int(input('Digite a terceira medida: '))
if t1 + t2 > t3 and t1 + t3 > t2 and t2 + t3 > t1:
    decisão= 'PODEM'
    print(f'As medidas {t1}, {t2}, {t3} {decisão} formar um triangulo')
else:
    decisão='NÃO PODEM'
    print(f'As medidas {t1}, {t2}, {t3} {decisão} formar um traingulo')
   
