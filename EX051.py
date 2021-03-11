primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a Razão: '))
te10 = primeiro + (10 - 1) * razao
for c in range(primeiro, te10 + razao, razao):
    print('{}'.format(c), end=' -> ')
print('ACABOU')
