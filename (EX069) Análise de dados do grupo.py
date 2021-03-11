homem = 0
maior = 0
mulhermenor20 = 0


while True:


    print('-' * 40)
    print('\033[1;31mCADASTRE UMA PESSOA\033[m')
    print('-' * 40)

    idade = int(input('IDADE: '))
    sexo = ' '

    while sexo not in 'MF':
        sexo = str(input('SEXO: [M/F] ')).upper().strip()[0]
    print('-' * 40)
    SN = ' '
    while SN not in 'SN':
        SN = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if idade >= 18:
            maior = maior + 1

    if sexo == 'F' and idade < 20:
            mulhermenor20 = mulhermenor20 + 1

    if sexo == 'Mm'.upper().strip()[0]:
            homem = homem + 1

    if SN == 'Nn'.upper().strip()[0]:
            break



print(f'Temos {maior} pessoas cadastradas que tem ou são maiores de 18 anos')
print(f'Temos {homem} Homens cadastrado na plataforma')
print(f'Temos ao todo {mulhermenor20} mulheres cadastradas que são menores de 20 anos ')


