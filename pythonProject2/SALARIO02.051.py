salario=float(input('Qual é o seu salario? '))
n1=salario*15/100+salario
n2=salario*10/100+salario
if salario>1250:
    print(f'Seu salario é {n2:.2f} reais')
else:
    print(f'Quem ganhava {salario:.2f} reais passa a ganhar {n1:.2f} reais')