altura = float(input('Qual é a sua altura? '))
peso = float(input('Qual é o seu peso? '))
imc = peso / (altura ** 2)
print('O imc dessa pessoa é de {:.1f}'.format(imc))
from time import  sleep
print('PROCESSANDO...')
sleep(1)
if imc < 18.5:
    print('Abaixo do peso')

elif imc > 18.5 and imc <= 25:
    print('Peso Ideal')

elif imc > 25 and imc <= 30:
    print('Sobrepeso')

elif imc > 30 and imc <=40:
    print('Obesidade')

elif imc > 40:
    print('Obesidade MÓRBIDA, \033[1;31mCUIDADO\033[m')
