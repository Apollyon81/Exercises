def div(n=0, formato=False):
    n=n/2
    return n if formato is False else moeda(n)

def dobro(n=0, formato=False):
    n=n*2
    return n if formato is False else moeda(n)

def percent(n=0, c=0, formato=False):
    n=n*c/100+n
    return n if formato is False else moeda(n)
def percentm(n=0, c=0, formato=False):
    n=n*(-c)/100+n
    return n if formato is False else moeda(n)
def moeda(x=0):
    n=f'R${x:.2f}'
    return n.replace('.', ',')

def resumo(valor, percen, percentmenor):
    print(f'A metade de {moeda(valor)} é {div(valor, True)}')
    print(f'O dobro de {moeda(valor)} é {dobro(valor, True)}')
    print(f'Aumentando {percen}% de {moeda(valor)} é {percent(valor, percen, True)}')
    print(f'Diminuindo {percentmenor}% de {moeda(valor)} é {percentm(valor, percentmenor, True)}')

def leia(msn):
    valido=False
    while not valido:
        entrada = str(input(msn).replace(',', '.').strip())
        if entrada.isalpha() or entrada=='':
            print(f'ERRO: "{entrada}" é um preço invalido')
        else:
            valido=True
            return float(entrada)