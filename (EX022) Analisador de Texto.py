nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em letras maisculas é {}'.format(nome.upper()))
print('Seu nome em letra minusculas é {}'.format(nome.lower()))
print('Seu nome completo tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))




