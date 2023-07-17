def inteiro(msn1):
    while True:
        try:
            ai=int(input(msn1))
        except ValueError:
            return 0
        except TypeError:
            print('ERRO: digite um valor valido!')
        except KeyboardInterrupt:
            print('\nO usuario preferiu não informar os dados')
            return None
        else:
             return ai
def flutuante(msn):
    ai = inteiro  # Chamamos a função inteiro aqui
    print(ai)
    if ai is None:  # Se o usuário interromper em inteiro, retorna None em flutuante
        return None
    while True:
        try:
            fi=float(input(msn))
        except ValueError:
            return 0
        except TypeError:
            print('ERRO: digite um valor valido!')
            return 0
        except KeyboardInterrupt:
            print('O usuario preferiu não informar os dados')
            return None
        except Exception as erro:
            print(f'O erro que ocorreu foi {erro}')
            continue
        else:
            return fi