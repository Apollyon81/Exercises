n=float(input('Quanto será pago pelo produto? '))
n1=str(input('Qual é a forma de pagamento? '))
n2=n1.lower()
n3=n-n/100*10
n4=n-n/100*5
n5=n+n/100*20
if 'dinheiro' in n2 or 'cheque' in n2:
    print(f'Você iria pagar {n} e terá que pagar {n3} com 10% de desconto')
elif 'vista' in n2 or 'cartão' in n2:
    print(f'Você vai pagar {n4} com 5% de desconto')
elif 'cartão' in n2 and ('2x' in n2 or '2 vezes' in n2):
    print(f'Você vai pagar {n} em 2x no cartão')
else:
    print(f'Você vai pagar {n5} em {n1}')