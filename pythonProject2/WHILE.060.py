#VALIDAÇÃO DE DADOS
'''n2=''
while True:
    n1=str(input('Qual é o seu sexo M/F: ')).lower().strip()[0]
    if n1=='m':
       n2='Homem'
    elif n1=='f':
        n2 = 'Mulher'
    else:
        print('Digite uma opção valida')
        continue
    print(f'Você é {n2}')
    break'''
#Enquanto não 02
'''n1=str(input('Qual é o seu sexo: [M/F] ')).strip().upper()[0]
while n1 not in 'MmFf':
    print('Digite uma opção VALIDA!')
    n1=str(input('Qual é o seu sexo: [M/F] ')).upper().strip()[0]
print(f'Sexo {n1} registrado')'''

#Sorteio > ou <
'''import random
tenta=0
dica=''
nume=random.randint(1, 10)
while True:
    n1=int(input('Escolha um numero de 1 a 10: '))
    if n1<nume:
        dica='Mais...'
    elif n1>nume:
        dica='Menos...'
    elif n1==nume:
        print(f'A maquina escolheu {nume}, Você acertou em {tenta+1} tentativas!')
        break
    if n1!=nume:    
        print(f'{dica}Tenta mais uma vez.')
        tenta+=1
        continue
    while not (n1>=1 or n1<=10):
        print('Digite uma opção valida')'''

'''#Criando menu de opções
text=''
soma=0
while True:
    n1=int(input('Digite o 1° valor: '))
    n2=int(input('Digite o 2° valor: '))
    opcao=int(input('Escolha uma opção:\n[1]Somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair do programa\nSua escolha: '))
    if opcao==1:
        soma=n1+n2
        text='soma'
    elif opcao==2:
        soma=n1*n2
        text='multiplicação'
    elif opcao==3:
         if n1>n2:
            soma=n1
         elif n2>n1:
            soma=n2
         else:
             if n1==n2:
                 print('Os numeros são iguais')
                 continue
         print(f'O maior valor é {soma}')
         continue
    elif opcao==4:
        continue
    elif opcao==5:
        print('Você escolheu sair do programa')
        break
    else:
       print('Escolha uma opção valida!')
       continue
    print(f'A {text} de {n1} e de {n2} é {soma}')'''

#fatorial fail
'''fato=1
n1=int(input('Digite qual numero você quer o fatorial: '))
while n1>=1:
    fato*=n1
    n1-=1
    if n1>=1:
        print(f'{n1[::-1]}x', end='')
print(f'O fatorial é {fato}')'''
#fatorial correto
'''fato = 1
n1 = int(input('Digite qual número você quer o fatorial: '))
multiplicacoes = []
while n1 >= 1:
    fato *= n1
    multiplicacoes.append(str(n1))
    n1 -= 1
print(f'{ " x ".join(multiplicacoes[::-1]) } = {fato}')'''

#PROGRESSÃO
'''print('GERADOR DE PA')
prime=int(input('Qual é o termo: '))
razao=int(input('Qual é a razão: '))
cont=1
termo=prime
while cont<=10:
    print(f'{termo}-->', end='')
    termo+=razao
    cont+=1
print('FIM')'''
    
#super PA
'''while True:
    n1 = int(input('Digite o primeiro termo: '))
    n2 = int(input('Digite a razão: '))
    termo=n1
    cont=1
    quant=0
    while cont<=10:
        print(f'{termo}-->', end='')
        termo+=n2
        cont+=1
        quant+=1
    print('PAUSA')
    n3=1
    while n3!=0:
        n3 = int(input('\nQuer mostrar mais quantos termos: '))
        if n3 == 0:
           break
        termo-=n2
        cont2=1
        while cont2 <= n3:
           termo+=n2
           print(f'{termo}-->', end='')
           cont2+=1
           quant+=1
        print('PAUSA')
    if n3==0:
        break
print(f'PROGRESSÃO FINALIZADA COM {quant} TERMOS')'''

#FIBONATI
'''n1=int(input('Quantos termos você quer mostrar: '))
un=0
bi=1
cont=2
print(f'{un}-->{bi}-->', end='')
while cont<n1:
    n3=un+bi
    print(f'{n3}-->', end='')
    un=bi
    bi=n3
    cont+=1
print('FIM')'''

#TRATANDO VARIOS VALORES
'''cont=0
valor=0
n1=int(input('Digite um valor: '))
while n1!=999:
    valor+=n1
    cont+=1
    n1 = int(input('Digite um valor: '))
print(f'Você digitou {cont} valores e a soma deles é {valor}')'''

#MAIOR E MENOR VALORES
r1='S'
maior=0
media=0
quant=0
soma=0
menor=0
while r1=='S':
    n1=int(input('Digite um número: '))
    soma+=n1
    quant+=1
    if quant==1:
        maior=menor=n1
    else:
        if n1>maior:
            maior=n1
        if n1<menor:
            menor=n1
    r1 = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]   
    media=soma/quant
print(f'Foram {quant} numeros, O maior numero foi {maior} a soma deles é {soma} e a media foi {media:.1f}\nO menor é {menor} e o maior é {maior}')
    

    
    
    




    
    
        
        




    
    
    
    




    
    
    