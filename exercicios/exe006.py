# Desafio 006
# Faça um algoritimo que leia um n~umero e mostre o seu dobro, triplo e raiz quadrada.

import math

numero = int(input('Informe um número: '))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada1 = math.sqrt(numero)
raiz_quadrada2 = numero ** (1/2)
raiz_quadrada3 = pow(numero, (1/2))

print(f'O dobro de {numero} é {dobro}')
print(f'O triplo de {numero} é {triplo}')
print(f'A raiz quadrada de {numero} é {raiz_quadrada1:.2f}')
print(f'A raiz quadrada de {numero} é {raiz_quadrada2:.2f}')
print(f'A raiz quadrada de {numero} é {raiz_quadrada3:.2f}')

