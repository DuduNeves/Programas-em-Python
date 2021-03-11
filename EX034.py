salario = float(input('Digite o valor do seu salario em R$ '))
ma = (10 / 100 * salario) + salario
me = (15 / 100 * salario) + salario

if salario > 1250.00:
    print('O seu salario com o aumento de 10% fica no valor de R${:.2f}'.format(ma))
else:
    print('Seu salario com o aumento de 15% fica no valor de R${:.2f}'.format(me))

