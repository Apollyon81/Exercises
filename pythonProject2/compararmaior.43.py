n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3= float (input('Digite o terceiro numero: '))

if n1>n2 and n1>n3:
    print(f"O primeiro número que é {n1}  é o maior.")
elif n2>n1 and n2>n3:
    print(f'O segundo numero que é {n2} é o maior')
else:
    print(f'O terceiro numero que é {n3} é o maior')