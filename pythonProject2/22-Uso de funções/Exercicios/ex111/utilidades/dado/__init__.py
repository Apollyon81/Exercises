def leia(msn):
    valido=False
    while not valido:
        entrada=str(input(msn)).strip().replace(',','.')
        if entrada.isalpha() or entrada=='':
            print(f'"{entrada}" Não é um valor valido')
        else:
            valido=True
            return float(entrada)
