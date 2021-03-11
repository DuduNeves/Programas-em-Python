'''from random import sample

#Com o Sample fica bem mais facil, pois colocando ele e quantidade que a gente quer ele já da a quantidade direto e não  é preciso fazer um tantto de vez, igual o exemplo de baixo do randint

sorteio = tuple(sample(range(10), 5))
print(sorteio)

print(f'O numero maior é o {max(sorteio)}')
print(f'O numero menor é o {min(sorteio)}')'''


#TEM UM MODO COM O FOR E VARIOS RANDINT, TIPO PRECISAMOS DE 5 NUMEROS ALEATORIOS VAMOS COLOCAR 5 RANDINT, PARA GEREAR 5 NUMEROS.


from random import randint

numero = (randint(1, 9)), (randint(1, 9)), (randint(1, 9)), (randint(1, 9)), (randint(1, 9))

for n in numero:
    print(f' {n}', end=' ')

print(f'\nO numero maior é {max(numero)}')
print(f'O numero menor é {min(numero)}')
