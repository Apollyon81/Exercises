nome=str(input('Qual é o seu nome? '))
if nome=='Taique':
    print('Que nome lindo você tem! ')
else:
    print('Seu nome é tão normal')
print(f'Bom dia, {nome}!')

nota=float(input('Digite a primiera nota: '))
nota1=float(input('Digite a segunda nota'))
n1=(nota+nota1)/2
print(f'Sua media foi {n1:.1f}')
if n1>=6.0:
    print(f'Sua média foi boa! PARABÉNS!')
else:
    print(f'Sua média foi ruim! ESTUDE MAIS!')
