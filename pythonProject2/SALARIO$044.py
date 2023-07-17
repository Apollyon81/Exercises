sala=float(input('Digite o salario: '))
n1=sala*10/100+sala
n2=sala*15/100+sala
if sala>1250:
    print(f'Seu salario é {n1}')
else:
    print(f'Seu salario é {n2}')