n1=float(input('Qual é adistancia da sua viagem? '))

if n1<200:
    n2=n1*0.50
    print(f'O custo da sua viagem é {n2:.2f} reais')
else:
    n3 = n1 * 0.45
    print(f'O custo da sua viagem é {n3:.2f} reais')