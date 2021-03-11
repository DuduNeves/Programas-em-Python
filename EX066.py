n = 0
soma = 0
cont = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    cont = cont + 1
    soma = soma + n
print(f'A soma dos {cont} valores digitados dá {soma}!')