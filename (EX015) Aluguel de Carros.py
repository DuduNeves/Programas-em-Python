dias = int(input('Quantos dias o carro foi alugado: '))
km = float(input('Quantos km rodados: '))
valD = 60 * dias
valKm = 0.15 * km
total = valD + valKm
print('O valor total a pagar é de R${:.2f}'.format(total))

