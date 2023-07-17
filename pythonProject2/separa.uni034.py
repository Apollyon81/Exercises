nume=(input('Informe um numero: '))
n1 = nume[0]
n2 = nume[1]
n3 = nume[2]
n4 = nume[3]
print(f"""Unidade: {n4}
Dezena: {n3}
Centena: {n2}
Milhar: {n1}""")

#PARA RECEBER EM INT
nume = int(input('Informe um número: '))
n1 = nume // 1000  # obtém o algarismo da casa dos milhares
n2 = (nume // 100) % 10  # obtém o algarismo da casa das centenas
n3 = (nume // 10) % 10  # obtém o algarismo da casa das dezenas
n4 = nume % 10  # obtém o algarismo da casa das unidades
print(f"""Unidade: {n4}
Dezena: {n3}
Centena: {n2}
Milhar: {n1}""")

      