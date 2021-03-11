'''print('Vou pensar em um numero entre 0 e 5, tente adivinha! ')
nU = int(input('Em que numero pensei: '))
from random import choice
from time import sleep
lista = [0 , 1 , 2 , 3 , 4 , 5]
es = choice(lista)
print('PROCESSANDO...')
sleep(2)
if nU == es:
    print('PARABÊNS! Você conseguiu ganhar')
else:
    print('ERROUUU! Eu pensei no numero {} e não no {}'.format(es, nU)'''





#ESSE DE BAIXO É MAIS PRATICO PARA MAIORES VALORES ALEATORIOS

from random import randint
from time import sleep

sn = str(input('Vamos jogar um jogo?')).upper()

if sn == 'SIM':
    print('Okay, Vou pensar em um numero entre 0 e 10, tente adivinha! ')
else:
    print('AFF QUE PENA')
    sleep(1)

nu = int(input('Em que numero pensei: '))
es = randint(0, 10)
print('PROCESSANDO...')
sleep(2)
if nu == es:
    print('PARABÊNS! Você conseguiu ganhar dessa hahaha ')
else:
    print('ERROUUU! TENTE NOVAMENTE'.format(es, nu))



