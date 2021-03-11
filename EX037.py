from time import sleep
num = int(input('Digite um numero inteiro: '))
print('\033[1;37mPROCESSANDO...\033[m')
sleep(2)
print('''\033[1;33mEscolha uma base de conversão:\033[m
 \033[1;35m[ 1 ] Converter para Binario\033[m
 \033[1;32m[ 2 ] Converter para Octal
 \033[1;34m[ 3 ] Converter para Hexadecimal\033[m''')

opcão = int(input('Sua opção: '))

print('\033[1;36mPROCESSANDO...\033[m')
sleep(2)

if opcão == 1:
    print('\033[1;35m{} convertido para BINARIO é igual á {}\033[m'.format(num, bin(num)[2:]))

elif opcão == 2:
    print('\033[1;32m{} convertido para OCTAL é igual á {}\033[m'.format(num, oct(num)[2:]))

elif opcão == 3:
    print('\033[1;34m{} convertido para HEXADECIMAL é igual á {}\033[m'.format(num, hex(num)[2:]))

else:
    print('\033[1;31mOPÇÃO INVALIDA, TENTE NOVAMENTE  \033[m')


