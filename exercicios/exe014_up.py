# Desafio 014
# Escreva um programa que converta uma temperatura digitada em °C e converta para °F
# Upgrade com a opção de escolher a escala inicial e um ajuste para utilizar menor linhas
# Ainda é possível um novo upgrade a partir da correção e também para acrescentar a opção de escolher a escala a ser convertido

temp = float(input('\nInforme a temperatura: '))

c_f = round(((temp * (9/5)) + 32),2)
c_k = round((temp + 273.15),2)

f_c = round(((temp - 32) * (5/9)),2)
f_k = round(((temp - 32) * (5/9) + 273.15),2)

k_c = round((temp - 273.15),2)
k_f = round(((temp - 273.15) * (9/5) + 32),2)

opcao = input('\nInforme a opção desejada, sendo "C" para Celsius, "F" para Fahrenheit ou "K" para Kelvin \n>>> ')


if opcao == 'C' or opcao == 'c':
    print(f'\n{temp}°C equivale a {c_f}°F e a {c_k}°K \n')
elif opcao == 'F' or opcao == 'f':
    print(f'\n{temp}°F equivale a {f_c}°C e a {f_k}°K \n')
elif opcao == 'K' or opcao == 'k':
    print(f'\n{temp}°K equivale a {k_c}°C e a {k_f}°F \n')
else:
    print('Opção Invalida.')