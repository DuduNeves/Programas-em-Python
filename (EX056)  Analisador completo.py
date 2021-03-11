somaidade = 0
maiorhomem = 0
maisvelho = ''
totfeminino = 0

for c in range(1, 5):
    print('----------{}°----------'.format(c))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('M/F: ')).strip()

    somaidade = somaidade + idade
    media = somaidade / c

    if c == 1 and sexo in 'Mm':
        maiorhomem = idade
        maisvelho = nome

    if sexo in 'Mm' and idade > maiorhomem:
        maiorhomem = idade
        maisvelho = nome

    if sexo in 'Fm' and idade < 20:
        totfeminino = totfeminino + 1


print('A media da idade do grupo foi de {}'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorhomem, maisvelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totfeminino))
