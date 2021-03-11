
primeiro = int(input('Digite o primeiro valor: '))
segundo = int(input('Digite o segundo valor: '))
opção = 0
 
while opção != 5:

    print('''
        [ 1 ] SOMAR
        [ 2 ] MULTIPLICAR
        [ 3 ] MAIOR
        [ 4 ] NOVOS NUMEROS
        [ 5 ] SAIR DO PROGRAMA
        ''')

    opção = int(input('Qual é a sua opção: '))
    if opção == 1:
        soma = primeiro + segundo
        print('O resultado da sua soma é \033[1;32m{}{}{}\033[m'.format('\033[1;32m', soma, '\033[m'))
    elif opção == 2:
        multiplicação = primeiro * segundo
        print('O resultado da sua multiplicação é {}'.format(multiplicação))
    elif opção == 3:
        if primeiro > segundo:
            maior = primeiro
        else:
            maior = segundo
        print('O valor maior entre {} e {} é {}'.format(primeiro, segundo,maior ))

    elif opção == 4:
        primeiro = int(input('Digite o primeiro valor: '))
        segundo = int(input('Digite o segundo valor: '))
    elif opção == 5:
         print('PROGRAMA ENCERRADO, OBRIGADO POR UTILIZAR')
    else:
        print('Opção invalida')