print('-=-' * 20)
print('SEQUÊNCIA DE FIBONACCI')
print('-=-' * 20)

n = int(input('Quantos termos você quer mostrar? '))
print('~~~' * 20)
penultimo = 0
ultimo = 1
print('~~~' * 20)
contador = 3
print('{} -> {}'.format(penultimo, ultimo),end=' ')
contador = 3

while contador <= n:
    termo = penultimo + ultimo
    print(' -> {}'.format(termo),end=' ')
    penultimo = ultimo
    ultimo = termo
    contador = contador + 1
print('-> FIM')
print('~~~' * 20)


'''DIFICIL'''
