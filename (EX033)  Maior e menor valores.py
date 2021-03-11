from time import sleep

#CORES

cores = { 'limpar':'\033[m',
          'branco':'\033[30m',
          'vermelho': '\033[31m',
          'verde':'\033[32m',
          'amarelo':'\033[33m',
          'azul':'34m',
          'roxo':'\033[35m',
          'ciano': '\033[46m',
          'cinza':'\033[36m'}


a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))
print('Vou calcular qual é o menor e o maior numero')
sleep(1)
print('\033[1;32mPROCESSANDO...\033[m')
sleep(2)

if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

print('O numero menor é o {}{}{}'.format(cores['amarelo'], menor, cores['limpar']))

if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O numero maior é o {}{}{}'.format(cores['verde'], maior, cores['limpar']))

