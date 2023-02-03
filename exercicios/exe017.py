# Desafio 017
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import sqrt, hypot

cateto_oposto = float(input('Informe o valor do cateto oposto: '))
cateto_adjacente = float(input('Informe o valor do cateto adjacente: '))
# hipotenusa = sqrt((cateto_oposto ** 2) + (cateto_adjacente ** 2))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print(f'O valor da hipotenusa é: {hipotenusa:.3f}')