simnao = 0
cont = 0
media = 0
maior = 0
menor = 0
soma = 0

while simnao != 'n'.upper():
    numero = int(input('Digite um numero: '))
    simnao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    cont = cont + 1
    soma = soma + numero
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero

media = soma / cont

print('Você digitou {} numeros e a media dos numeros digitadors foram de {}'.format(cont,media))
print('O maior numero digitado foi {} e o menor numero digitado foi {}'.format(maior, menor))
