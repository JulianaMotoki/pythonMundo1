# Desafio 0112
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Informe o preço do produto: '))
desconto = preco * 0.05
preco_novo = preco - desconto

print(f'O novo valor do produto é R${preco_novo}')
