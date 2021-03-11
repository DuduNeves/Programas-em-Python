numero = int(input('Digite um numero qualquer, para saber se ele é PAR ou IMPAR: '))
resultado = numero % 2
from time import sleep
print('PROCESSANDO...')
sleep(2)
if resultado == 0:
    print('O numero {} é PAR.'.format(numero))
else:
    print('O numero {} é IMPAR.'.format(numero))

