n1=float(input('Valor da casa: '))
n2=int(input('Vai em quantos anos? '))
n3=int(input('Qual é o seu salario? '))
n4=n1/n2/12
n5=n3/100*30
if n5>=n4:
    print(f'A parcela será de {n4:.2f} e 30% do seu salario que é {n5} Reais \n CORRESPONDE COM A MENSALIDADE DA CASA!!!')
else:
    print('EMPRESTIMO NEGADO!!!')