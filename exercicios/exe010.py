# Desafio 010
# Crie um programa que leia quanto dinheiro tem na carteira e mostre quantos Dólares ela pode comprar.

dinheiro_carteira = float(input('Informe quanto dinheiro você tem em sua carteira: '))
cotacao_dolar = float(input('Informe a cotação do Dólar hoje: '))
cotacao_euro = float(input('Informe a cotação do Euro hoje: '))
dolar = dinheiro_carteira * cotacao_dolar
euro = dinheiro_carteira * cotacao_euro

print(f'Com R${dinheiro_carteira:.2f}, você pode comprar ${dolar:.2f} ou €{euro:.2f}')