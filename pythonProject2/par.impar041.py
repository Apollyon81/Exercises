par=int(input('Digite um numero: '))
if par % 2 == 0:
    print(f'O numero {par} é par')
else:
    print(f'O numero {par} é impar')
    
km=float(input('Quantos km é o seu destino? '))
n1=km*1/2
n2=km*(0.45)
if km>=200:
    print(f'Sua distancia é {km} portanto será cobrado {n2} reais')
else:
    print(f'Sua distancia é {km} portando será cobrado {n1} reais')
