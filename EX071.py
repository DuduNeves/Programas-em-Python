from time import sleep

print('\033[1;35m=' * 40)
print(' ' * 10, 'BANCO DO DUDU', ' ' * 10 )
print('=' * 40)

valor = int(input('\033[mQual o valor você quer sacar? R$: ' ))

total = valor
cedula = 200
totcedulas = 0



while True:
    if total >= cedula:
        total-=cedula
        totcedulas += 1
    else:
        if totcedulas > 0:
            sleep(1)
            print(f'{totcedulas} CÉDULAS DE {cedula} REAIS')
        if cedula == 200:
            cedula = 100
        elif cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 1
        totcedulas = 0
        if total == 0:
            break

print('\033[1;35m=' * 40)
print(' ' * 10, 'OBRIGADO E ATÉ LOGO', ' ' * 10)
print('=' * 40)


#ESTUDAR ESSE DEPOIS, ESTUDAR MAIS LÓGICA TAMBEM

