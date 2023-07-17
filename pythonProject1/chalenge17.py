import random
n1=int (input('Diga o nome do 1°Aluno: '))
n2=int (input('Diga o nome do 2°Aluno: '))
n3=int (input('Diga o nome do 3°Aluno: '))
n4=int (input('Diga o nome do 4°Aluno: '))
n5=random.randint(n1, n4)
print(f'O ganhador é {n5}')