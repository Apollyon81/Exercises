#107-Exercitando modulos em python
from ex111.utilidades import moeda
from ex111.utilidades import dado
'''n1=float(input('Digite um valor: R$'))
print(f'O dobro de {n1} é {dobro(n1)}')
print(f'A metade de {n1} é {metade(n1)}')
print(f'Aumentando 10% de {n1} é {mpercent(n1, 10)}')
print(f'Diminuindo 15% de {n1} é {percentm(n1, 15)}')'''


#108/109-Formatando em python
'''n1=float(input('Digite um valor: R$'))
print(f'O dobro de {moeda(n1)} é {dobro(n1, True)}')
print(f'A metade de {moeda(n1)} é {moeda(metade(n1))}')
print(f'Aumentando 10% de {moeda(n1)} é {moeda(mpercent(n1, 10))}')
print(f'Diminuindo 15% de {moeda(n1)} é {moeda(percentm(n1, 15))}')'''

#110-Reduzindo o programa
'''n1=float(input('Digite um valor: R$'))
moeda.resumo(n1, 20, 12)'''

#111-Instrução de pacote

#112-Entrada de dados mone
# tarios
p=dado.leia('Digite um valor: R$')
moeda.resumo(p, 35, 22)

