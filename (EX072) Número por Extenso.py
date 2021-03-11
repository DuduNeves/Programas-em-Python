print('-' * 60)
print(' ' * 10, 'DESCUBRA SEU NUMERO POR EXTENSO', ' ' * 10)
print('-' * 60)

cont = 0
numero = int(input('Digite um numero entre 0 e 20: '))
numeros = ('zero', 'um', 'dois', 'três','quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while numero < 0 or numero > 20:
    numero = int(input('Digite um numero entre 0 e 20: '))

print('-=-' * 20)
print(f'\033[1;35mVocê digitou o numero {numeros[numero]}\033[m')

while True:
    print('-=-' * 20)
    SN = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    print('-=-' * 20)
    if SN == 'Ss'.upper().strip()[0]:
        numero = int(input('Digite um numero entre 0 e 20: '))
        print('-=-' * 20)
        print(f'\033[1;35mVocê digitou o numero {numeros[numero]}\033[m')

    if SN == 'Nn'.upper().strip()[0]:
        print('Muito obrigado por usar o programa ')
        break
