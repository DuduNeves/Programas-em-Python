'''from math import sqrt
CaOp = float(input('Qual o comprimento do cateto oposto: '))
CaAd = float(input('Qual o coprimento do cateto adiacente: '))
hipo = sqrt(CaOp ** 2 + CaAd ** 2)
print('O valor da hipotenusa é de {:.2f} '.format(hipo))'''

from math import hypot
Co = float(input('Qual o comprimento do cateto oposto: '))
Ca = float(input('Qual o comprimento do cateto adiacente: '))
hi = hypot(Co, Ca)
print('O comprimento da hipotenusa é igual a {:.2f}'.format(hi))





