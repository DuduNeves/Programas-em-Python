numero = 0
soma = 0
cont = 0
while numero != 999:
    numero = int(input('Digite um numero ou DIGITE 999 PARA PARAR: '))
    cont = cont + 1
    soma = soma + numero
    somax = soma - 999
    contx = cont - 1

print('Você digitou {} numeros e a soma dos numeros digitados é de {}'.format(contx, somax))