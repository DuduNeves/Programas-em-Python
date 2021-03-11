from time import sleep
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
print('\033[1;32mPROCESSANDO...\033[m')
sleep(2)
if n1 > n2:
    print('O PRIMEIRO numero é maior')
elif n2 > n1:
    print('O SEGUNDO numero é maior')

elif n1 == n2 or n2 == n1:
    print('Os DOIS numeros são iguais')
