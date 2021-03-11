print('\033[1;33m-' *40)
print(' ' * 10, 'LOJA SUPER BARATÃO', ' ' * 10)
print('-' * 40)

cont = 0
soma = 0
maior1000 = 0
menor = 0
barato = ' '


while True:

    nome = str(input('\033[mNome do produto: '))
    preco = float(input('Preço: R$: '))

    cont = cont + 1
    soma = soma + preco

    if preco > 1000:
        maior1000 = maior1000 + 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = nome

    SN = ' '
    while SN not in 'SN':
        print('-' * 40)
        SN = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    print('-' * 40)

    if SN == 'Nn'.upper().strip()[0]:
        break

print('\033[1;33m-' *40)
print(' ' * 10, 'FIM DA COMPRA', ' ' * 10)
print('-' *40)


print(f'\033[mO total da sua compra foi de R${soma:.2f}')
print(f'Temos {maior1000} produtos maiores que R$ 1.000,00')
print(f'O produto mais barato comprado foi {barato} no valor de R${menor:.2f}')

