print('{:=^40}'f'LOJAS BABEL')
n=float(input('Qual é o valor do produto: '))
n1=int(input('ESCOLHA A FORMA DE PAGAMENTO \n[ 1 ] Á vista dinheiro/cheque \n[ 2 ] Á vista cartão \n[ 3 ]  2x no cartão \n[ 4 ]  3x ou mais no cartão\nOpção: '))
n2=n-n*10/100
n3=n-n*5/100
n4=n
n5=n+n*20/100
if n1==1:
    print(f'O preço de R${n:.2f} será R${n2:.2f} á partir da forma de pagamente que você escolheu')
elif n1 == 2:
        print(f'O preço de R${n:.2f} será R${n3:.2f} á partir da forma de pagamente que você escolheu')
elif n1 == 3:
        print(f'O preço de R${n:.2f} será R${n4:.2f} á partir da forma de pagamente que você escolheu')
elif n1 == 4:
        print(f'O preço de R${n:.2f} será R${n5:.2f} á partir da forma de pagamente que você escolheu')
else:
    print('ESCOLHA UMA OPÇÃO VALIDA')
    
preco=float(input('Qual é o valor do produto: '))
forma=int(input('ESCOLHA A FORMA DE PAGAMENTO \n[ 1 ] Á vista dinheiro/cheque \n[ 2 ] Á vista cartão \n[ 3 ]  2x no cartão \n[ 4 ]  3x ou mais no cartão\nOpção: '))
if forma==1:
    total=preco*0.90
elif forma==2:
    total=preco*0.95
elif forma == 3:
    total = preco
elif forma==4:
    total=preco*1.20
if forma in [1, 2, 3, 4]:
    print(f'O produto vale R${preco:.2f} mas \ná partir da forma de pagamento que você escolheu você pagará R${total:.2f}')
else:
    print('ESCOLHA UMA FORMA DE PAGAMENTO VALIDA')

