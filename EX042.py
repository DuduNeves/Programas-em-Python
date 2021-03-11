from time import sleep
print('-=-' * 20)
print('ANALISANDO TRIANGULOS...')
print('-=-' * 20)
a = float(input('Digite o primeiro segmento:'))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))
print('CALCULANDO...')
sleep(1.5)
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triangulo ')
    sleep(1.5)
    if a == b == c:
        print('PROCESSANDO...')
        sleep(1.5)
        print('ESSE TRIÂNGULO É EQUILÁTERO!!!')

    elif a == b or a == c or b == a or b == c:
        print('PROCESSANDO...')
        sleep(1.5)
        print('ESSE TRIÂNGULO É ISÓSCELES!!!')

    elif a != b != c:
        print('PROCESSANDO...')
        sleep(1.5)
        print('ESSE TRIÂNGULO É ESCALENO!!!')


else:
    print('Os segmentos acima NÃO PODEM FORMAR um triangulo')

