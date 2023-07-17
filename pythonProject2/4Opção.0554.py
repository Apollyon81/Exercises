n1=int(input('Em que ano você nasceu? '))
n2=2023-n1
if n2<=9:
    print(f'Você tem {n2} anos portanto participará da categoria MIRIM!')
elif n2>9 and n2<=14:
    print(f'Sua idade é {n2}, portando participara da categoria INFANTIL!')
elif n2>14 and n2<=19:
    print(f'Sua idade é {n2}, portando participara da categoria é JUNIOR!')
else:
    print(f'Sua idade é {n2}, portando participara da categoria é MASTER!')
    