frase = str(input('Digite uma frase: ')).strip().upper()
a = frase.count('A')
print('A letra A aparece {} vezes nessa frase.'.format(a))
p = frase.find('A') +1
print('A letra "A" aparece na posição {} pela primeira vez nessa frase.'.format(p))
u = frase.rfind('A') +1
print('A letra "A" aparece pela ultima vez na posição {} nessa frase.'.format(u))



