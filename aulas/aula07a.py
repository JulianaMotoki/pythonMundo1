# nome = input('Qual é o seu nome? ')
# print('Prazer em te conhecer {:20}!'.format(nome))
# print('Prazer em te conhecer {:<20}!'.format(nome))
# print('Prazer em te conhecer {:>20}!'.format(nome))
# print('Prazer em te conhecer {:^20}!'.format(nome))
# print('Prazer em te conhecer {:=^20}!'.format(nome))


n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

so = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# print('A soma vale {}'.format(n1+n2))

print(f'A soma é {so}, \n a subtração é {su}, \n o produto é {m} e a divisão é {d:.3f}', end='. ')
print(f'Já a divisão inteira é {di} e a potência é {e}')
