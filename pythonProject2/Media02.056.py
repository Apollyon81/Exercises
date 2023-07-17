n1=float(input('Qual foi sua media no primeiro semestre: '))
n2=float(input('Qual foi sua media no segundo semestre: '))
n3=(n1+n2)/2
if n3<=5:
    print(f'No 1° semestre você tirou {n1} e 2° semestre você tirou {n2} \nSua media foi {n3:.1f} Você esta REPROVADO')
elif n3>5 and n3<=6.9:
    print(f'No 1° semestre você tirou {n1} e 2° semestre você tirou {n2} \nSua media foi {n3:.1f} Você esta em RECUPERAÇÃO')
elif n3>7:
    print(f'No 1° semestre você tirou {n1} e 2° semestre você tirou {n2} \nSua media foi {n3:.1f} Você esta APROVADO')
    