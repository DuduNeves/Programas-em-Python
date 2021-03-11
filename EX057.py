
s = 0
while s != 'M' and s != 'F':
    s = str(input('Digite seu sexo [M/F]: ')).upper().strip()
    if s == 'M' or s == 'F':
         print('Parabens seu sexo foi registrado com sucesso')
    else:
        print('Tente  novamente, sexo não registrado')
