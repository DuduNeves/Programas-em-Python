cont = 0
par = 0


n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite mais um numero: '))
n4 = int(input('Digite o ultimo numero: '))
numeros = (n1, n2, n3, n4)
print(f'Os numeros digitados foram: {numeros}')

cont = cont + 1


print(f'O numero 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1}° posição')
else:
    print('O numero 3 não existe nos numeros digitados ')
print('Os valores pares digitados foram: ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=', ')
