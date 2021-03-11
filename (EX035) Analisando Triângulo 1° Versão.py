
print('-=-' * 20)
print('ANALISANDO TRIANGULOS...')
print('-=-' * 20)
a = float(input('Digite o primeiro segmento:'))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triangulo ')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triangulo')

''''#definindo o maior

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

  #definindo o menor

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#Definindo o segundo menor

menor2 = a <= menor
if b <= menor:
    menor2 = b
if c <= menor:
    menor2 = c


triangulo = (menor + menor2) > maior


if triangulo == True:
    print('Os segmentos acima PODEM FORMAR um triangulo ')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triangulo')'''
