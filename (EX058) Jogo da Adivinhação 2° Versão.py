from random import randint
from time import sleep
computador = randint(0, 10)

decisão = str(input('Você quer jogar? ')).upper().strip()

if decisão == 'SIM':
    print('Sou seu computador...acabei de pensar em um numero entre 0 e 10')
    sleep(1)
    print('Será que você consegue adivinhar qual foi?')
    sleep(1)
    acertou = False
    palpites = 0
    while not acertou:
        jogador = int(input('Digite seu palpite: '))
        palpites = palpites + 1
        if jogador == computador:
            acertou = True
        else:
            if jogador < computador:
                print('Chuta mais alto')
            else:
                print('Chuta mais baixo')
    print('Parabens você acetou com {} tentativas'.format(palpites))
else:
    print('Que pena MEDROSO')
