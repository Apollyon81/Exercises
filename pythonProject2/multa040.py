carro=float(input('Quantos Km o inviduo ultrapassou? '))
n1=carro*7
if carro>=80:
    print(f'Sua velocidade ultrapassou 80km e terá que pagar {n1}')
else:
    print(f'Sua velocidade foi {carro} portanto esta dentro das normas')
