from _datetime import date
n1=int(input('Em que ano você nasceu? '))
n2=date.today().year
n3=n2-n1
n4=18-n3
print(f'Quem nasceu em {n1} tem {n3} anos em {n2}')
if n3>=18 and n3<24 :
    print(f'Você tem {n3} anos e esta na hora de se alistar!!!')
elif n3>=24:
    print(f'Você tem {n3} anos e passou da hora de se alistar!!!')
else:
    print(f'Você tem {n3} anos e falta ainda {n4} anos para se alistar')
    