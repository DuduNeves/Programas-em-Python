nome = input('\033[1;32m Digite seu nome: \033[m')
print('Prazer em te conhecer', '\033[1;31m', nome, '\033[m')
idade = int(input('Quantos anos você tem? '))
print("\033[1;30m A você é novo ainda, com {}{}{} \033[1;30m anos tem uma vida toda pela frente".format('\033[1;34m', idade, '\033[m'))


