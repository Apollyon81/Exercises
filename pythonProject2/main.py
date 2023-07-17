import random

n1 = []
n2 = []
n3 = []
n4 = []
n1.append(input('Diga o nome do 1°Aluno: '))
n2.append(input('Diga o nome do 2°Aluno: '))
n3.append(input('Diga o nome do 3°Aluno: '))
n4.append(input('Diga o nome do 4°Aluno: '))
n5 = random.choice([n1, n2, n3, n4])
print(f'O ganhador é {n5}')

from random import choice, sample
aluno1 = str(input('Digite o nome do aluno 1: '))
aluno2 = str(input('Digite o nome do aluno 2: '))
aluno3 = str(input('Digite o nome do aluno 3: '))
aluno4 = str(input('Digite o nome do aluno 4: '))
n_trabs = int(input('Digite quantos trabalhos serão apresentados hoje: '))
print(f'O aluno escolhido para apagar o quadro foi: {choice([aluno1, aluno2, aluno3, aluno4])}')
print(f'A ordem de apresentação dos trabalhos será: {sample([aluno1, aluno2, aluno3, aluno4], k=n_trabs)}')





