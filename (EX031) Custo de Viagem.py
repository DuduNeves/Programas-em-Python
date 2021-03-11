distancia = float(input('Qual a distancia da sua viagem em Km\h: '))
print('Você está prstes a começar uma viagem de {}Km\h'.format(distancia))
ate2 = 0.50 * distancia
ate3 = 0.45 * distancia
from time import sleep
print('PROCESSANDO...')
sleep(2)
if distancia <= 200:
    print('O preço da sua passagem é de R${:.2f}'.format(ate2))
else:
    print('O preço da sua passagem é de R${:.2f}'.format(ate3))
