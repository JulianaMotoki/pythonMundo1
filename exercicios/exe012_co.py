# Desafio 0112
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
# Correção a partir do que foi passado pelo professor, para diminuir o numero de variaveis

preco = float(input('Informe o preço do produto: R$'))
preco_novo = preco - (preco * 0.05)

print(f'O produto que custava R${preco:.2f}, na promoção com desconto de 5% vai custar R${preco_novo:.2f}')
