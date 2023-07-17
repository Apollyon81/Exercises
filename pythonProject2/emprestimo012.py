casa=float(input('Qual é o valor da casa que deseja: '))
salario=float(input('Qual é o seu salario: '))
anos=int(input('Em quantos anos deseja pagar a casa: '))
from time import sleep
print('\033[45m CARREGANDO \033[m')
sleep(2)
n1=salario/100*30
n2=casa/anos/12
if n1<=n2:
    print(f'Infelimente 30% do seu salario que é {n1:.2f} \n não condiz com a mensalidade de {n1:.2f} reais da casa')
else:
    print(f'30% do seu salario que é {n1:.2f} Reais condiz com a mensalidade da casa de {n2:.2f} Reais')
    
