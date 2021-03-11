from time import sleep
print('\033[1;32mVAMOS CALCULAR SEU EMPRESTIMO...\033[m')
sleep(1)

valor = float(input('Qual o valor da casa? '))

salario = float(input('Qual seu salario? '))

anos = int(input('Em quantos anos você deseja pagar? '))

print('\033[1;32mCALCULANDO...\033[m')
sleep(2)

sa30 = 30 / 100 * salario
anom = anos * 12
valot = valor / anom
if valot <= sa30:
    print('Para pagar a sua casa de R${:.2f} em {} anos, a prestação será de R${:.2f} por mês.'.format(valor, anos, valot))
    print('\033[1;32mPROCESSANDO...\033[m')
    sleep(2)
    print('\033[1;33mEMPRESTIMO CONSEDIDO\033[m')

else:
    print('Para pagar a sua casa de R${:.2f} em {} anos, a prestação será de R${:.2f} por mês'.format(valor, anos, valot))
    print('\033[1;32mPROCESSANDO...\033[m')
    sleep(2)
    print('\033[1;31mEMPRESTIMO NEGADO\033[m')
