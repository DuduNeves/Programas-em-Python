from random import randint

v = 0


print('-=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR?')
print('-=-' * 20)

while True:

    valor = int(input('Digite um valor: '))
    computador = randint(0, 10)
    soma = valor + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
        print(f'Você jogou {valor} e o computador {computador} e o resultado deu {soma}')
        print('DEU PAR'if soma % 2 == 0 else 'DEU ÍMPAR')
        print('-' * 40 )

    if tipo == 'P':
        if soma % 2 == 0:
            print('Você ganhou!!!')
            v = v + 1
        else:
            print('Você perdeu :(')
            break

    elif tipo == 'I':
        if soma % 2 == 1:
            print('Você venceu!!!')
            v = v + 1
        else:
            print('Você perdeu :(')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER... Você venceu {v} vezes')



#DIFICIL A QUESTÃO DA LOGICAAAAAAA



