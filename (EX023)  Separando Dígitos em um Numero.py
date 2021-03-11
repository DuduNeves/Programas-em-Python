numero = int(input('Digite um numero: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('O numero {} tem a unidade {}'.format(numero, u))
print('O numero {} tem a desena {}'.format(numero, d))
print('O numero {} tem a centena {}'.format(numero, c))
print('O numero {} tem o milhar {}'.format(numero, m))

