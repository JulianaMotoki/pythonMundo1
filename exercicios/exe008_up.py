# Desafio 008
# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
# Upgrade - Converter Metros em seus múltiplos (quilômetro, hectômetro e decâmetro) e submúltiplos (decímetro, centímetro milímetro).

metro = float(input('Informe a quantidade de metros: '))
quilometro = metro / 10
hectometro = metro / 100
decametro = metro / 1000
decimetro = metro * 10
centimetro = metro * 100
milimetro = metro * 1000

print(f'{metro}m equivale a:\n{quilometro:.2f}km \n{hectometro:.2f}hm \n{decametro:.2f}dam \n{decimetro:.0f}dm \n{centimetro:.0f}cm \n{milimetro:.0f}mm')

