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

print('Unidades de Medida para Conversão \n1 - Quilômetro (km) \n2 - Hectômetro (hm) \n3 - Decâmetro (dam) \n4 - Decímetro (dm) \n5 - Centímetro (cm) \n6 - Milímetro (mm)')

opcao = int(input('Escolha a unidade de medida a ser calculada: '))

match (opcao):
    case 1:
        print(f'{metro}m equivale a {quilometro:.2f}km')
    case 2:
        print(f'{metro}m equivale a {hectometro:.2f}hm')
    case 3:
        print(f'{metro}m equivale a {decametro:.2f}dam')
    case 4:
        print(f'{metro}m equivale a {decimetro:.0f}dm')
    case 5:
        print(f'{metro}m equivale a {centimetro:.0f}cm')
    case 6:
        print(f'{metro}m equivale a {milimetro:.0f}mm')
