# Desafio 011
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
# Exercicio com ajustes a partir da correção e conhecimento do curso Basico de Python
# Necessário ajuste para quando a quantidade de tinta na lata for maior que a área a ser pintada

import math

largura = float(input('Informe a largura da parede em metros: '))
altura = float(input('Informe a altura da parede em metros: '))
qtd_lata = float(input('Informe a quantidade de litros da lata de tinta: '))
area = largura * altura

qtd_tinta = area / qtd_lata
lata = round(qtd_tinta)

print(f'Sua parede tem dimensão de {largura} x {altura} e sua área é de {area}m²')
print(f'Para pintar sua parede é necessário {qtd_tinta} litros de tinta. \nNecessário comprar {lata} latas de tinta de {qtd_lata} litros')
