# Desafio 008
# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

metro = float(input('Informe a quantidade de metros: '))
centimetro = metro * 100
milimetro = metro * 1000

print(f'{metro}m equivale a {centimetro:.0f}cm e a {milimetro:.0f}mm')