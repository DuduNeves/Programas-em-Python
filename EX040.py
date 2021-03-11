from time import sleep
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

print('\033[1;32mCALCULANDO...\033[m')
sleep(1)

print('Tirando {:.1f} e {:.1f} a media do Aluno é de {:.1f}'.format(nota1, nota2, media))
sleep(1)

print('\033[1;32mPROCESSANDO...\033[m')
sleep(2)

if media >= 7.0:
    print('Parabêns, você está \033[1;33mAPROVADO\033[m')

elif media >= 5.0 and media < 7.0:
    print('Não foi dessa vez, mas fique tranquilo você ainda tem a \033[1;35mRECUPEÇÃO.\033[m')

elif media < 5.0:
    print('Sinto muito mais você está \033[1;31mREPROVADO\033[m, estude mais')
