import random
n1=str(input('JOKENPO!!!: '))
n2='pedra','papel', 'tesoura'
n4=random.choice(n2)
if n4=='papel' and n1=='papel':
    print(f'Maquina: {n4}' '\n EMPATE!!!')
if n4=='pedra' and n1=='pedra':
    print(f'Maquina: {n4}' '\n EMPATE!!!')
if n4=='tesoura' and n1=='tesoura':
    print(f'Maquina: {n4}' '\n EMPATE!!!')
elif n4=='tesoura' and n1=='papel':
    print(f'MAQUINA: {n4} \n VOCÊ PERDEU!!!')
elif n4=='tesoura' and n1=='pedra':
    print(f'MAQUINA: {n4} \n VOCÊ GANHOU!!!')
elif n4=='pedra' and n1=='papel':
    print(f'MAQUINA: {n4} \n VOCÊ GANHOU!!!')
elif n4=='pedra' and n1=='tesoura':
    print(f'MAQUINA: {n4} \n VOCÊ PERDEU!!!')
elif n4=='papel' and n1=='pedra':
    print(f'MAQUINA: {n4} \n VOCÊ PERDEU!!!')
elif n4=='papel' and n1=='tesoura':
    print(f'MAQUINA: {n4} \n VOCÊ GANHOU!!!')
else:
    print('POR FAVOR ESCOLHA ENTRE PAPEL, PEDRA E TESOURA!!!')

     
