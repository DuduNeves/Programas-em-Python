from datetime import date
ano = date.today().year
tomaior = 0
tomenor = 0
for c in range(1, 8):
    pessoa = int(input('Digite o ano de nascimento da {}° pessoa: '.format(c)))
    idade = ano - pessoa
    if idade >= 18:
        tomaior = tomaior + 1
    else:
        tomenor = tomenor + 1

print('Ao todo tivemos {} pessoas maiores de idade e {} menos de idade'.format(tomaior, tomenor))

