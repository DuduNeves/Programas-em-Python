#MODO BEM MAIS FACIL DE SE FAZER COM O FOR

while True:

    print('-' * 40)
    numero = int(input('Quer ver a tabuada de qual valor? ' ))
    print('-' * 40)

    if numero < 0:
        break

    for c in range(1, 11):
        print(f'{numero} x {c} = {numero*c}')




print('Programa encerrado. Obrigado por utilizar')

#MODO DIFICIL DE SE FAZER 1 A 1

'''   x1 = numero * 1
    x2 = numero * 2
    x3 = numero * 3
    x4 = numero * 4
    x5 = numero * 5
    x6 = numero * 6
    x7 = numero * 7
    x8 = numero * 8
    x9 = numero * 9
    x10 = numero * 10

    print(f'{numero} x 1 = {x1}')
    print(f'{numero} x 2 = {x2}')
    print(f'{numero} x 3 = {x3}')
    print(f'{numero} x 4 = {x4}')
    print(f'{numero} x 5 = {x5}')
    print(f'{numero} x 6 = {x6}')
    print(f'{numero} x 7 = {x7}')
    print(f'{numero} x 8 = {x8}')
    print(f'{numero} x 9 = {x9}')
    print(f'{numero} x 10 = {x10}') '''

