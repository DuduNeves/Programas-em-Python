genero = str(input('Você é Homem ou Mulher? ')).upper().strip()
if genero == 'HOMEM':
    from datetime import date
    ano = int(input('Digite o ano em que você nasceu: '))
    ano0 = date.today().year
    total = ano0 - ano

    if total == 18:
        print('Quem nasceu em {} tem {} anos e deve se alistar IMEDIATAMENTE'.format(ano, total))

    elif total < 18:

        saldo = 18 - total
        anot = ano0 + saldo
        print('Ainda falta {} anos para o alistamento'.format(saldo))
        print('Seu alistamento será em {}'.format(anot))

    elif total > 18:

        saldo1 = total - 18
        anotm = ano0 - saldo1
        print('Você deveria ter se alistado há {} anos'.format(saldo1))
        print('Seu alistamento foi em {}'.format(anotm))
elif genero == 'MULHER':
    print('Desculpa mas o serviço militar obrigatorio é só para Homens')

else:
    print('Desculpe,esse genero é desconhecido')