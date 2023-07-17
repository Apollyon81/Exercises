#frase = input('Digite uma frase: ')
#n1 = frase.find('a')
#n2 = frase.rfind('a')
#n3 = frase.count('a')
#print(f"O 'a' aparece {n3} vezes e o primeiro 'a' está na posição {n1} e o último 'a' está na posição {n2}.")

nome=str(input(f'Digite uma frase: '))
n1=nome.strip()
n2=n1.lower()
nome=n2.replace('á', 'a')
n1=nome.count('a')
n2=nome.find('a')+1
n3=nome.rfind('a')
print(f"""A letra A aparece {n1} vezes na frase
A primeira possivel da letra A é {n2}
E a sua ultima posição é {n3}""")