from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
ano0 = date.today().year
idade = ano0 - ano
from time import sleep
print('PROCESSANDO...')
sleep(2)
if idade <= 9:
    print('Você tem {} anos e está na categoria Mirim'.format(idade))

elif idade > 9 and idade <= 14:
    print('Você tem {} anos e está na categoria Infantil'.format(idade))

elif idade > 14 and idade <= 19:
    print('Você tem {} anos e está na categoria Junior'.format(idade))

elif idade > 19 and idade <= 25:
    print('Você tem {} anos e está na categoria Senior'.format(idade))

elif idade > 25:
    print('Você tem {} anos e está categoria Master'.format(idade))
