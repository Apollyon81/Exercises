n1=float(input('Qual foi sua nota: '))
n2=float(input('Qula foi sua segunda nota: '))
n3=(n1+n2)/2
if n3<=5:
    print(f'Sua média foi {n3:.1f}, você esta reprovado')
elif n3>5 and n3<= 6.9:
    print(f'Sua media foi {n3:.1f} portanto esta em recuperação')
else:
    print(f'Sua média doi {n3:.1f} você esta aprovado!!!')