#Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostra uma mensagem com a data formatada.

dia = input('Dia = ')
mes = input('Mês = ')
ano = input('Ano = ')
print('Você nasceu no dia ' + dia + ' do ' + mes + ' de ' + ano + '.')
print(f'Você nasceu em {dia}/{mes}/{ano}')
