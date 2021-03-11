from time import sleep
from random import randint

itens = print('Pedra', 'Papel', 'Tesoura')
escolhido = randint(0, 2)
print('Suas opçoes: \n[ 0 ]Pedra\n[ 1 ]Papel\n[ 2 ]Tesoura')

joga = int(input('Qual vai ser a sua jogada? '))


print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print(20 * '-=-')
  
print('O computador escolheu {}'.format(escolhido))

print('Você escolheu {}'.format(joga))

print(20 * '-=-')

if escolhido == 0 and joga == 2:
    print('COMPUTADOR VENCEU!!!')
elif escolhido == 0 and joga == 0:
    print('EMPATE!!!')
elif escolhido == 0 and joga == 1:
    print('VOCÊ VENCEU!!!')
elif escolhido == 2 and joga == 0:
    print('VOCÊ VENCEU!!!')
elif escolhido == 2 and joga == 2:
    print('EMPATE!!!')
elif escolhido == 2 and joga == 1:
    print('COMPUTADOR VENCEU!!!')
elif escolhido == 1 and joga == 0:
    print('COMPUTADOR VENCEU!!!')
elif escolhido == 1 and joga == 1:
    print('EMPATE!!!')
elif escolhido == 1 and joga == 2:
    print('VOCÊ GANHOU!!!')
else:
    print('Desculpa essa opção não existe, tente novamente')










