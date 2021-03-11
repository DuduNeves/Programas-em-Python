from time import sleep
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro: '))
print('\033[1;32mPROCESSANDO...\033[m')
sleep(2)
s = n1 + n2
print('A soma entre {} e {} é igual a {}'.format(n1, n2, s))







