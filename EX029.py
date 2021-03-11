velo = float(input('Qual velocidade você estava? '))
multa = (velo - 80) * 7
if velo <= 80:
    print('Velocidade permitida, have a nice trip')
else:
    print('VELOCIDADE PERMITIDA DE 80Km/h ULTRAPASSADA!!! Você foi multado no valor de R${:.2f}'.format(multa))




