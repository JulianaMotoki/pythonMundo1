# Desafio 011
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

largura = float(input('Informe a largura da parede em metros: '))
altura = float(input('Informe a altura da parede em metros: '))
metro_quadrado = largura * altura

qtd_tinta = metro_quadrado / 2

print(f'Para pintar {metro_quadrado}m² de parede, será necessária {qtd_tinta} de latas de tinta')
