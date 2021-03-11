pr = float(input('Qual o preço do produto que você quer? R$'))
des = 5 / 100 * pr
fi = pr - des
print('Esse seu produto está com 5% de desconto, olha que legal!!! \nO preço dele agora sai por R${:.2f}. '.format(fi))
