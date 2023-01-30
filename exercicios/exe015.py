# Desafio 015
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
# Exercício + Correção

dias = int(input('Informe a quantidade de dias: '))
km = float(input('Informe a distância percorrida: '))

valor_total = (dias * 60) + (km * 0.15)

print(f'O total a pagar é de R${valor_total:.2f}')