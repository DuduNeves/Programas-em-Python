print('\033[1;31m-=-\033[m' * 20)

termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão:  '))

termo10 = termo
contador = 0
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while contador < total:
        print('{} -> '.format(termo), end=' ')
        termo = termo + razao
        contador = contador + 1
    print('PAUSA')
    mais = (int(input('Quantos termos você quer mostrar mais? ')))
print('Progressão finalizada com {} termos mostrados'.format(total))

