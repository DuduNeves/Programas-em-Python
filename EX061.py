print('\033[1;31m-=-\033[m' * 20)

termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão:  '))

termo10 = termo
contador = 1


while contador < 11:
    print('{} -> '.format(termo), end=' ')
    termo = termo + razao
    contador = contador + 1
print('FIM')

'''DIFIIL PARA CARALHO PRECISO ESTUDAR MAIS O WHILE E FOR'''