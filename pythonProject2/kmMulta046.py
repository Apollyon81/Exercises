n1=float(input('Qual é a velocidade atual do carro? '))
if n1>80:
    n2=(n1-80)*7   
    print(f'Você excedeu o limite de velocidade em {n1}km e deverá pagar {n2:.2f} reais de multa')
else:
    print('Você esta dentro do limite de velocidade')