from time import sleep
numero = int(input('Digite um numero: '))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[34m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')

    print('{}'.format(c), end=' ')
    sleep(0.5)
print('\n\033[mO numero {} foi divisivel {} vezes'.format(numero, total))
print('-=-' * 20)
if total == 2:
    sleep(2)
    print('O numero {} é primo'.format(numero))

else:
    sleep(2)
    print('O numero {} não é primo'.format(numero))

