#107
import Matematica
'''num=int(input('Digite um numero: '))
print(f'A metade de {num} é {Matematica.div(num)}')
print(f'O dobro de {num} é {Matematica.dobro(num)}')
print(f'Aumentando 10% de {num} é {Matematica.percent(num, 10)}')
print(f'Diminuindo 13% de {num} é {Matematica.percentm(num, 13)}')'''

#108/109 como moeda
'''num=float(input('Digite um valor: R$'))
print(f'A metade de {Matematica.moeda(num)} é {Matematica.div(num, True)}')
print(f'O dobro de {Matematica.moeda(num)} é {(Matematica.dobro(num, True))}')
print(f'Aumentando 10% de {Matematica.moeda(num)} é {Matematica.percent(num, 10, True)}')
print(f'Diminuindo 13% de {Matematica.moeda(num)} é {Matematica.percentm(num, 13, True)}')'''

#110
'''p=float(input('Digite um valor: R$'))
Matematica.resumo(p, 80, 35)'''

#111-se dar erro
n1=Matematica.leia('Digite o preço: R$')
Matematica.resumo(n1, 50, 25)