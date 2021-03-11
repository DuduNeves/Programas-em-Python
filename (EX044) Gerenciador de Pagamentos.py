print(20 * '=', 'LOJA DO DUDU', 20 * '=')
preco = int(input('Qual o preço do produto: '))
print('Formas de pagamento\n [ 1 ] Á vista no dinheiro/cheque\n [ 2 ] Á vista no cartão de credito\n [ 3 ] 2x no cartão\n [ 4 ] 3x ou + no cartão')
vistadc = preco - (10 / 100 * preco)
vistaca = preco - (5 / 100 * preco)
cartão3x = (20 / 100 * preco) + preco
op = int(input('Qual será sua opção: '))

if op == 1:
    print('A vista você ganha 10% de desconto de o produto sai por R${:.2f}'.format(vistadc))
elif op == 2:
    print('A vista no cartão você ganha 5% de desconto e o produto sai por R${:.2f}'.format(vistaca))
elif op == 3:
    cartão2x = preco / 2
    print('Em 2x no cartão de credito o preço do produto fica normal e fica R${:.2f} por mês'.format(cartão2x))
elif op == 4:
    print('Em 3x ou mais ou no cartão, você paga um juros de 20%, ficando no valor de R${:.2f}'.format(cartão3x))
else:
    print('Sinto muito mas essa opção não existe, tente novamente nas outras.')
