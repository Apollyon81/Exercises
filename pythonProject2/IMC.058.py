peso=float(input('Qual é a seu peso (Kg) '))
altura=float(input('Qual é a sua altura (m) '))
imc=peso/(altura**2)
print(f'O IMC dessa pessoa é {imc:.1f}')
if imc<18.5:
    print('Você está abaixo do peso normal')
elif imc>=18.5 and imc <25:
    print('Parabéns, você está na faixa de PESO NORMAL')
elif imc>=25 and imc < 30:
    print('Você está com SOBREPESO')
elif imc>=30 and imc<40:
    print('Você está com OBESIDADE!')
elif imc>=40:
    print('Você está com OBESIDADE, CUIDADO!')