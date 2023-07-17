def dobro(nim, formato=False):
    nim=nim*2
    return nim if formato is False else moeda(nim)
def metade(nim, formato=False):
    nim=nim/2
    return nim if formato is False else moeda(nim)
def mpercent(nim, num, formato=False):
    nim=(nim*num/100)+nim
    return nim if formato is False else moeda(nim)
def percentm(nim, num, formato=False):
    nim=(nim*(-num)/100)+nim
    return nim if formato is False else moeda(nim)
def moeda(nim=0):
    nim=f'R${nim:.2f}'
    return nim.replace('.',',')

def resumo(valor=0,taxamais=10, taxamenos=5):
    print('-'*34)
    print('RESUMO DO VALOR'.center(34))
    print('-'*34)
    print(f'Preço analisado: {moeda(valor)}')
    print('-'*34)
    print(f'Dobro de {moeda(valor)}: \t\t{dobro(valor, True)}')
    print(f'Metade de {moeda(valor)}: \t{moeda(metade(valor))}')
    print(f'Aumentando {taxamais}%: \t\t{moeda(mpercent(valor, taxamais))}')
    print(f'Diminuindo {taxamenos}%: \t\t{moeda(percentm(valor, taxamenos))}')
    print('-'*34)

def leia(msn):
    while not msn.isdigit():
        valor=input(msn)
        return valor
